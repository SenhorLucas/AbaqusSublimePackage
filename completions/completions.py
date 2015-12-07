import sublime
import sublime_plugin

ST3 = int(sublime.version()) > 3000

import os


class DictionaryAutoComplete(sublime_plugin.EventListener):
    settings = None
    b_first_edit = True
    b_fully_loaded = True
    word_list = []

    # on first modification in comments, get the dictionary and save items.
    def on_modified(self, view):
        if self.b_first_edit and self.b_fully_loaded:
            self.b_fully_loaded = False
            sublime.set_timeout(lambda: self.load_completions(view), 3)

    def load_completions(self, view):
        scope_name = view.scope_name(view.sel()[0].begin())       # sublime.windows()[0].active_view()
        if self.should_trigger(scope_name):
            words = ["avocado","annanas"]
            for word in words:
                self.word_list.append(word)
            self.b_first_edit = False
        else:
            self.b_fully_loaded = True

    # This will return all words found in the dictionary.
    def get_autocomplete_list(self, word):
        autocomplete_list = []
        for w in self.word_list:
            autocomplete_list.append((w, w))
        return autocomplete_list

    def should_trigger(self, scope):
        if "abaqus" in scope or "string.quoted" in scope:
            return True
        return False

    # gets called when auto-completion pops up.
    def on_query_completions(self, view, prefix, locations):
        scope_name = sublime.windows()[0].active_view().scope_name(sublime.windows()[0].active_view().sel()[0].begin())
        if self.should_trigger(scope_name):
            return self.get_autocomplete_list(prefix)