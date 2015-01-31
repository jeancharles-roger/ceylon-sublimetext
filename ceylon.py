import sublime, sublime_plugin

import os.path
import re

class CompileCeylonCommand(sublime_plugin.WindowCommand):
   def run(self, cmd = [], file_regex = "", line_regex = "", working_dir = "",
            encoding = "utf-8", env = {}, quiet = False, kill = False,
            path = "", # Catches "path" and "shell"
            **kwargs):

      working_dir = os.path.abspath(working_dir)
      selection_path = os.path.abspath(cmd.pop())

      # Navigates throught parents to find the first module.ceylon file.
      parent_path = os.path.dirname(selection_path)
      while len(parent_path) > 0:
         module_path = parent_path + '/module.ceylon';
         if ( os.path.exists(module_path) ):
            break;
         parent_path = os.path.dirname(selection_path)
      
      if ( os.path.exists(module_path) ):
         # If module file found, searches for module name

         # The regex to use
         pattern = re.compile("^\\s*module\\s*\\b([a-zA-Z0-9\\.]+)\\b")

         # Searches the module file
         module_name = None
         module_file = open(module_path)
         line = module_file.readline()
         while len(line) > 0:
            matched = pattern.match(line)
            if matched:
               module_name = matched.group(1)
               break;
            line = module_file.readline()
         
         module_file.close()

         # Checks for module name
         if module_name:
            cmd.append(module_name)
            print "[Ceylon] Compiling the module '" + module_name +"'."
         else:
            print "[Ceylon] Module file '"+ module_path +"' isn't valid, cancelling compilation."
            return;

      else:
         # Else, reset the command.
         cmd.append(selection_path)
         print "[Ceylon] Compiling the file '" + os.path.basename(selection_path) +"'."

      # Delegate compilation command to exec.
      self.window.run_command("exec", {
				"cmd": cmd,
				"working_dir": working_dir,
            "path": path
			})


class CeylonAutocomplete(sublime_plugin.EventListener):
   def on_query_completions(self, view, prefix, locations):
         if not view.match_selector(locations[0], "source.ceylon"):
            return []

   		#TODO
         print "-----------------"
   		#print "Locations: " + str(locations)
         print "Scope: " + view.scope_name(locations[0])
         #print "-----------------"
         return []


