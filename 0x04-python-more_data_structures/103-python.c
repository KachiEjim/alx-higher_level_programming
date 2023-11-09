#include <Python.h>



/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * 
 * @p: A PyObject byte object.
 * 
 */

void print_python_bytes(PyObject *p)
{
        unsigned char i, len;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  len: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size > 10)
                len = 10;
        else
                len = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %d bytes: ", len);
        for (i = 0; i < len; i++)
        {
                printf("%02hhx", bytes->ob_sval[i]);
                if (i == (len - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}


/**
 * print_python_list - Prints basic info about Python lists.
 * 
 * @p: A PyObject list object.
 * 
 */

void print_python_list(PyObject *p)
{
        int len, memSize, i;
        const char *type;
        PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;

        len = var->ob_size;
        memSize = list->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", len);
        printf("[*] Allocated = %d\n", memSize);

        for (i = 0; i < len; i++)
        {
                type = list->ob_item[i]->ob_type->tp_name;
                printf("Element %d: %s\n", i, type);
                if (strcmp(type, "bytes") == 0)
                        print_python_bytes(list->ob_item[i]);
        }
}
