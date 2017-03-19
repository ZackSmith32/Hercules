import sys
import os
import shutil # file operations copying

os.system('clear');


'''
	Intro text && getting project name
'''
sys.stdout.write("This script will create a new project direcory\n");
sys.stdout.write("Directory will be created in ~/\n\n");
sys.stdout.write("Press ENTER to continue\n");
sys.stdin.readline()
sys.stdout.write("Project name: ");
project_name = sys.stdin.readline();
project_name = project_name[:-1]

if len(project_name) == 0:
	print "no project name"
	exit()

'''
	Create the dir && sub dirs
'''
home_path = os.path.expanduser('~')
new_dir_path = home_path + '/' + project_name 
if not os.path.exists(new_dir_path):
	print "Directory created: " + new_dir_path
	os.makedirs(new_dir_path)
	os.makedirs(new_dir_path + '/' + 'includes')
	os.makedirs(new_dir_path + '/' + 'srcs')
	os.makedirs(new_dir_path + '/' + 'libdir')
	shutil.copy('Makefile', new_dir_path + '/Makefile')
else:
	#continue? yes ok, no exists
	print "Directory already exists"
	exit()

'''
	Update Makefile
'''
def update_makefile(search_str, insert_text):
	i = 0
	f = open(new_dir_path + '/Makefile', 'r+')
	makefile_contents = f.readlines()
	for line in makefile_contents:
		if search_str in line:
			makefile_contents[i] = makefile_contents[i][:-1]
			makefile_contents[i] += insert_text
			print makefile_contents[i]
			f.seek(0)
			break ;
		i += 1
	f.writelines(makefile_contents)
	f.close

update_makefile("NAME	=", '	' + project_name + '\n')

open(new_dir_path + '/.gitignore', 'w')
'''
	list of files to be added under the LIBFILES section of make files
'''
libs_for_makefile = ""

sys.stdout.write("libft? ")
libft_lib = sys.stdin.readline()
libft_lib = libft_lib[:-1]
if len(libft_lib) == 0:
	print "no response"
elif libft_lib == "y":
	shutil.copy(home_path + '/' + 'libft_dir/libft/libft.h', new_dir_path + '/includes')
	os.symlink(home_path + '/' + 'libft_dir/libft/libft.a', new_dir_path + '/libdir/libft.a')
	libs_for_makefile += "libft.a"


sys.stdout.write("printf? ")
printf_lib = sys.stdin.readline()
printf_lib = printf_lib[:-1]
if len(printf_lib) == 0:
	print "no response"
elif printf_lib == "y":
	shutil.copy(home_path + '/' + 'printf/includes/ft_printf.h', new_dir_path + '/includes')
	os.symlink(home_path + '/' + 'printf/libftprintf.a', new_dir_path + '/libdir/libftprintf.a')
	libs_for_makefile += " libftprintf.a"

sys.stdout.write("vector? ")
vector_lib = sys.stdin.readline()
vector_lib = vector_lib[:-1]
if len(vector_lib) == 0:
	print "no response"
elif vector_lib == "y":
	shutil.copy(home_path + '/' + 'vect/includes/vect.h', new_dir_path + '/includes')
	os.symlink(home_path + '/' + 'vect/libvect.a', new_dir_path + '/libdir/libvect.a')
	libs_for_makefile += " libvect.a"

sys.stdout.write("array? ")
array_lib = sys.stdin.readline()
array_lib = array_lib[:-1]
if len(array_lib) == 0:
	print "no response"
elif array_lib == "y":
	shutil.copy(home_path + '/' + 'libarray/includes/libarray.h', new_dir_path + '/includes')
	os.symlink(home_path + '/' + 'libarray/libarray.a', new_dir_path + '/libdir/libarray.a')
	libs_for_makefile += " libarray.a"

if len(libs_for_makefile) != 0:
	print "putting libs in makefile"
	update_makefile("LIBFILES=", '	' + libs_for_makefile + '\n')






