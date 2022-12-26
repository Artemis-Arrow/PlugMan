#this is a script to help manage plugins in neovim and tmux
#if you want to add more apps that this can be used to manage plugins for feel free
#to do so, I hope you would find this script helpful, do note that this script relies
#on 2 files that contain a list of neovim and tmux plugins, please feel free to add to them
#any plugin you want
#made by Artemis-Arrow
import sys
try:
    import fuzzysearch
except ModuleNotFoundError:
    import os
    print("module fuzzysearch not found, installing")
    os.system("pip3 install fuzzysearch")
    sys.exit

def ExtData(file, operation, plugin):
    file = open(file, 'r')
    data = file.readlines()
    names = []
    links = []
    for i in data:
        names.append(i.split(' ')[0])
        links.append(i.split(' ')[1])
    if operation == "install":
        pluginloc = names.index(plugin)
        pluglink = links[plugloc]
        return pluglink
    elif operation == "search":
        print("not yet implemented")

def InstallPlugin(app, path, file, plugin):
    link = ExtData(file, "install", plugin)
    if app == "nvim":
        linestart = "Plug "
    elif app == "tmux":
        linestart = "set -g @plugin "
    PluginCallLine = linestart + link
    f = open(path, 'rw')
    data = f.readlines
    if app == "nvim":
        insertline = data.index("call plugin#begin()")
    elif app == "tmux":
        insertline = 0
    writeline = linestart + link
    data.insert(insertline+1, writeline)
    data.close



args = sys.argv
del args[0]
try:
    app = args[0]
    operation = args[1]
    if operation == "install":
        plugin = args[2]
    else:
        plugin = 0
except IndexError:
    print("invalid arguments")

if app == "nvim":
    file = "nvimplugs.txt"
    path = "~/.config/nvim/init.vim"
elif app == "tmux":
    file = "tmuxplug.txt"
    path = "~/.tmux.conf"

link = ExtData(file, operation, plugin )

