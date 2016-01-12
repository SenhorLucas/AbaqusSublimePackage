import sublime, sublime_plugin

class RemoveEmptyCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regex = '\*\*\s*\n'
        regions = self.view.find_all(regex, sublime.IGNORECASE)
        for region in reversed(regions):
            self.view.erase(edit, region)

class RemoveAllCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regex = '\*\*.*\n'
        regions = self.view.find_all(regex, sublime.IGNORECASE)
        for region in reversed(regions):
            self.view.erase(edit, region)