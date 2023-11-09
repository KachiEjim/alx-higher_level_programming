#include <Python.h>


void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);


/**
 * print_python_bytes - Prints information about Python bytes objects
 * 
 * @p: Pointer to a Python object (PyObject)
 * 
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, len, i;
	char *s;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = ((PyBytesObject *)p)->ob_base.ob_size;
		s = ((PyBytesObject *)p)->ob_sval;
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", s);

		len = size < 10 ? size + 1 : 10;
		printf("  first %zd bytes:", len);
		for (i = 0; i < len; ++i)
		{
			printf(" %02x", (unsigned char)s[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints information about Python list objects
 * 
 * @p: Pointer to a Python object (PyObject)
 * 
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, memeSize, i;
	PyListObject *list;
	PyObject *item;
	const char *name;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		list = (PyListObject *)p;
		memeSize = list->allocated;
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", memeSize);

		for (i = 0; i < size; i++)
		{
			item = list->ob_item[i];
			name = item->ob_type->tp_name;
			printf("Element %zd: %s\n", i, name);
			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}