#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), i = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("Size of the Python List = %d\n", size);
	printf("Allocated = %ld\n", obj->allocated);
	while (i < size)
	{
		printf("Element %d : %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}