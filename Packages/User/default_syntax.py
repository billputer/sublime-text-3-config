import sublime, sublime_plugin

class DefaultSyntaxCommand(sublime_plugin.EventListener):
  def on_load(self, view):
    in_workspace = view.file_name().startswith('/Users/billwiens/src/workspace/')
    syntax_is_plain = view.settings().get('syntax') =='Packages/Text/Plain text.tmLanguage'
    if in_workspace and syntax_is_plain:
      view.set_syntax_file('Packages/YAML/YAML.tmLanguage')