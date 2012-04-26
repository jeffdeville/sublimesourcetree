import locale
import os
import subprocess
import sublime, sublime_plugin

class SourcetreeOpenCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return True

    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message(__name__ + ': No place to open Source Tree to')
            return False

    def run(self, *args):
        sublime.status_message(__name__ + ': running')
        path = self.get_path()
        if not path:
            sublime.status_message(__name__ + ': No path')
            return False
        if os.path.isfile(path):
            path = os.path.dirname(path)
    
        settings = sublime.load_settings('Base File.sublime-settings')
        stree_path = settings.get('stree_path', '/usr/local/bin/stree')

        if not os.path.isfile(stree_path):
            mac_path = '/Applications/SourceTree.app'
            if os.path.isdir(mac_path):
                stree_path = mac_path
            else:
                stree_path = None

        if stree_path in ['', None]:
            sublime.error_message(__name__ + ': stree executable path not set, incorrect or no stree?')
            return False

        if stree_path.endswith(".app"):
            subprocess.call(['open', '-a', stree_path, path])
        else:
            p = subprocess.Popen([stree_path], cwd=path.encode(locale.getpreferredencoding(do_setlocale=True)), shell=True)