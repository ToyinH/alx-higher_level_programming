#include <Python.h>
/**
 * print_python_list_info - C function that prints
 * some basic info about Python lists
 * @p: list
 *
 * Description
 * Py_SIZE: fnc to get size of object.
 * Typecast pyobject to PyListObject to access allocated within
 * the structure to get memory allocated.
 * Loop thru the list to get each element via its index.
 * PyList_GetItem fnx to get item which a PyObject then the type using
 * Py_TYPE fnx which returns a pointer to a struct
 * and tp_name for the name of the item
 *
 */
void print_python_list_info(PyObject *p)
{
	int size, mem_alloc, i;
	PyListObject *list;
	PyObject *item;

	/* Py_SIZE: fnc to get size of object */
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
