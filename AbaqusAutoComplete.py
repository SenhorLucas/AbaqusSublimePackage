import sublime, sublime_plugin

class AbaqusAutoComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        wordlist=[]
        scope = sublime.windows()[0].active_view().scope_name(sublime.windows()[0].active_view().sel()[0].begin())
        if "contact-pair" in scope:
            if "type" in scope:
                wordlist = [['SURFACE TO SURFACE'], ['NODE TO SURFACE']]
            elif "adjust" in scope:
                wordlist = [['YES'], ['NO']]
            elif "midface-nodes" in scope:
                wordlist = [['YES'], ['NO']]
            elif "minimum-distance" in scope:
                wordlist = [['YES'], ['NO']]
            elif "sliding-transition" in scope:
                wordlist = [['ELEMENT ORDER SMOOTHING'], ['LINEAR SMOOTHING'], ['QUADRATIC SMOOTHING']]
            elif "suplementary-constrains" in scope:
                wordlist = [['YES'], ['NO'], ['SELECTIVE']]
            elif "tracking" in scope:
                wordlist = [['PATH'], ['STATE']]
            if "value" not in scope:
                wordlist=[
                    ['INTERACTION'],
                    ['TYPE'],
                    ['ADJUST'],
                    ['SMALL SLIDING'],
                    ['EXTENSION ZONE'],
                    ['GEOMETRIC CORRECTION'],
                    ['HCRIT'],
                    ['MIDFACE NODES'],
                    ['MINIMUM DISTANCE'],
                    ['NO THICKNESS'],
                    ['SMOOTH'],
                    ['SLIDING TRANSITION'],
                    ['SUPLEMENTARY CONSTRAINS'],
                    ['TIED'],
                    ['TRACKING'],
                ]

        return wordlist