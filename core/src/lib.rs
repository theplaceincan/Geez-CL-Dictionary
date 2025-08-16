use pyo3::prelude::*;
use pyo3::types::PyModule;

#[pymodule]
fn geezcore(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello, m)?)?;
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
