
import os

lectures = [
'getting_set_up',                  # 1
'open_source_world',               # 2
'linux_command_line',              # 3
'more_on_the_command_line',              # 4
'basic_shell_scripting',                 # 5
'version_control_with_git',              # 6
'collaborative_version_control',               # 7
'branches_remotes_and_conflicts',              # 8
'working_with_python',              # 9
'python_calculator',                # 10
'python_structure',                 # 11
'modules_and_code_organization',           # 12
'test_driven_development',              # 13
'survey_of_numpy',                         # 14
'template',                         # 15
'scipy_and_sparse_systems',                # 16
'survey_of_scipy',                         # 17
'template',                         # 18
'object_oriented_programming',             # 19
'more_on_oop',                      # 20
'template',
'graphical_user_interfaces',        # 22
'gui_slots_and_signals',            # 23
'gui_embedded_graphics']

modules = {'basic_cpp': ['core', 'arrays', 'stl'],
           'oo_cpp': ['classes', 'inheritance', 'std'],
           'binary': ['data', 'formats', 'viz'],
           'text': ['processing', 'regex', 'formats'],
           'static_viz': ['mpl', 'format', 'beyond']}


tmpl = 'python convert_to_canvas.py ../pages/{}.md lec{}.html'

for i in range(len(lectures)):
    print(tmpl.format(lectures[i], i+1))
    os.system(tmpl.format(lectures[i], i+1))


tmpl = 'python convert_to_canvas.py ../pages/{}.md {}.html'
for mod in modules:
    for les in modules[mod]:
        name = '{}_{}'.format(mod, les)
        print(tmpl.format(name, name))
        os.system(tmpl.format(name, name))

os.system('python convert_to_canvas.py ../README.md syllabus.html')
os.system('rm tmp.html')

print('done!')
