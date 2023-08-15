#include <python3.10/Python.h>
/**
 *
 *
 */
void print_python_list_info(PyObject *p)
{
	int size, mem_alloc, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	list = (PyListObject *)p;
	mem_alloc = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem_alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
