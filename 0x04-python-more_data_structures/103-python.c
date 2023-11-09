#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_bytes(PyObject *p)
{
	ssize_t byte_size;
	ssize_t index;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &byte_size);


	printf("  size: %li\n", byte_size);
	printf("  trying string: %s\n", str);
	if (byte_size < 10)
		printf("  first %li bytes:", byte_size + 1);
	else
		printf("  first 10 bytes:");
	for (index = 0; index <= byte_size && index < 10; index++)
		printf(" %02hhx", str[index]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
	ssize_t list_size = PyList_Size(p);
	ssize_t index;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (index = 0; index < list_size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %li: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
	}
}
