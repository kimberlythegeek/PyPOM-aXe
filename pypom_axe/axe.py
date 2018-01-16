# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from pypom import Page
import os
import json
import time

_DEFAULT_SCRIPT = os.path.join(os.path.dirname(__file__), 'src', 'axe.min.js')


class AxePage(Page):

    def inject(self):
        """
        Recursively inject aXe into all iframes and the top level document.

        :param script_url: location of the axe-core script.
        :type script_url: string
        """
        with open(_DEFAULT_SCRIPT) as f:
            self.selenium.execute_script(f.read())

    def execute(self, context=None, options=None):
        """
        Run axe against the current page.

        :param context: which part of the page to analyze.
        :param options: dictionary of aXe options.
        """
        template = 'return axe.run(%s).then(function(result){return result;});'
        args = ''

        # If context parameter is passed, add to args
        if context is not None:
            args += '%r' % context
        # Add comma delimiter only if both parameters are passed
        if context is not None and options is not None:
            args += ','
        # If options parameter is passed, add to args
        if options is not None:
            args += '%s' % options

        command = template % args
        response = self.selenium.execute_script(command)
        return response

    def impact_included(self, rule, impact):
        """
        Function to filter for violations with specified impact level, and all
        violations with a higher impact level.
        """
        if impact == 'minor' or impact is None:
            return True
        elif impact == 'serious':
            if rule['impact'] != 'minor':
                return True
        elif impact == 'critical':
            if rule['impact'] == 'critical':
                return True
        else:
            return False

    def run(self, context=None, options=None, impact=None):
        """
        Inject aXe, run against current page, and return rules & violations.
        """
        self.inject()
        data = self.execute(context, options)
        violations = dict((rule['id'], rule) for rule in data['violations']
                          if self.impact_included(rule, impact))

        return violations

    def wait_for_page_to_load(self, context=None, options=None, impact=None):
        super(AxePage, self).wait_for_page_to_load()
        violations = self.run(context, options, impact)
        t = time.strftime("%m_%d_%Y_%H-%M-%S")
        title = self.selenium.title
        self.write_results('results/%s_%s.json' % (title, t), violations)
        assert len(violations) == 0, self.report(violations)

    def report(self, violations):
        string = ''
        string += 'Found ' + str(len(violations)) + ' accessibility violations:'
        for violation, rule in violations.items():
            string += '\n\n\nRule Violated:\n' + rule['id'] + ' - ' + rule['description'] + \
                '\n\tURL: ' + rule['helpUrl'] + \
                '\n\tImpact Level: ' + rule['impact'] + \
                '\n\tTags:'
            for tag in rule['tags']:
                string += ' ' + tag
            string += '\n\tElements Affected:'
            i = 1
            for node in rule['nodes']:
                for target in node['target']:
                    string += '\n\t' + str(i) + ') Target: ' + target
                    i += 1
                for item in node['all']:
                    string += '\n\t\t' + item['message']
                for item in node['any']:
                    string += '\n\t\t' + item['message']
                for item in node['none']:
                    string += '\n\t\t' + item['message']
            string += '\n\n\n'

        return string

    def write_results(self, name, output):
        """
        Write JSON to file with the specified name.

        :param name: Name of file to be written to.
        :param output: JSON object.
        """
        with open(name, 'w+') as f:
            f.write(json.dumps(output, indent=4))
