#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *element;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    unsigned char *bytes = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02hhx", bytes[i]);
        if (i < size - 1 && i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

