import sublime, sublime_plugin

class AbaqusAutoComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        print(view.file_name())
        wordlist = [['foofoo', 'foofoo'], ['foobar', 'foobar']]
        return wordlist
