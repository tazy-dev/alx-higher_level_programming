#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	ssize_t list_size = PyList_Size(p);
	ssize_t index;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (index = 0; index < list_size; index++)
	{
		printf("Element %li: %s\n", index, list->ob_item[index]->ob_type->tp_name);
	}
}
