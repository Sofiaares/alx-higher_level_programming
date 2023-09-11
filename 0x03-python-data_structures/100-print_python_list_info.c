#include "Python.h"

/**
* print_python_list_info - Prints basic information about a Python list
* @p: Pointer to the Python list object
*
* This function prints the size, allocated slots, and types of elements
* in the given Python list.
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t list_size = PyList_Size(p);
Py_ssize_t list_allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", list_allocated);

for (Py_ssize_t i = 0; i < list_size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *item_type = Py_TYPE(item)->tp_name;

printf("Element %ld: %s\n", i, item_type);
}
}
 7 changes: 7 additions & 0 deletions7  
0x03-python-data_structures/11-delete_at.py
@@ -0,0 +1,7 @@
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for item in my_list:
        del(my_list[idx])
        return my_list
