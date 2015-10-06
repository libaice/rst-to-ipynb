# Test file for notedown's handling of indented fenced code blocks

Those may typically occur within an itemize or so.

A normal fenced input/output:
```{.python .input}
1+1
```
```{.json .output}
[{"execution_count": 1, "output_type": "execute_result", "data": {"text/plain": "2"}, "metadata": {}}]
```

1.  Start of an itemize  
    An indented fenced input/output:

    ```{.python .input}
    1+1
    ```
    ```{.json .output}
    [{"execution_count": 1, "output_type": "execute_result", "data": {"text/plain": "2"}, "metadata": {}}]
    ```

    Another one:

    ```{.python .input}
    1+1
    ```
    ```{.json .output}
    [{"execution_count": 1, "output_type": "execute_result", "data": {"text/plain": "2"}, "metadata": {}}]
    ```

1.  Next item (should be numbered 2.)
