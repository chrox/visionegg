%module gl_qt
%{

#if defined(MS_WINDOWS)
#  include <windows.h>
#endif

#include "gl_qt.h"
#include "movieconvert.h"

PyObject *PyErr_GL_QTError; /* Errors generated by OpenGL/QuickTime code */
%}

%init %{
  /* New exception for GL_QT code */
  PyErr_GL_QTError = PyErr_NewException( "VisionEgg.QuickTime.GL_QTError", NULL, NULL ); // New reference
  Py_INCREF(PyErr_GL_QTError);
%}

%exception {
  $action
  if (gl_qt_err_occurred()) {
    PyErr_SetString(PyErr_GL_QTError, gl_qt_err_message());
    return NULL;
  }
}

%typemap(in) Movie theMovie {
  MovieObj_Convert($input,&$1);
};

gl_qt_renderer* gl_qt_renderer_create( Movie theMovie, unsigned tex_shape, float tex_scale ); // tex_scale = 0.0 is auto
void gl_qt_renderer_delete( gl_qt_renderer *);
void gl_qt_renderer_update( gl_qt_renderer *);

