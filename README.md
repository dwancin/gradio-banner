
# `gradio_banner`
<div style="display: flex; gap: 7px;">
  <a href="https://pypi.org/project/gradio-banner/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/gradio-banner"></a>
  <a href="https://huggingface.co/spaces/dwancin/gradio_banner" target="_blank"><img alt="Demo" src="https://img.shields.io/badge/%F0%9F%A4%97%20Demo-%23097EFF?style=flat&logoColor=black"></a>
  <a href="https://github.com/dwancin/gradio-banner" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/Repository-white?logo=github&logoColor=black"></a>
</div>

A banner component for displaying important information, alerts, notifications, and types of messages within a Gradio Blocks.

![screenshot](https://raw.githubusercontent.com/dwancin/gradio-banner/main/assets/preview.png)

## Installation

```bash
pip install gradio_banner
```

## Usage

```python

import gradio as gr
from gradio_banner import Banner

with gr.Blocks() as demo:
    with gr.Row():
        Banner(value="Large info banner *with* **markdown** `value`", variant="info")
    with gr.Row():
        Banner(variant="success", size="sm")
    with gr.Row():
        Banner(value="Large warning banner with default label and specified value", variant="warning")
    with gr.Row():
        Banner(variant="error", show_close_button=True)
    with gr.Row():
        with gr.Column():
            with gr.Row():
                Banner(value="Small info banner with close button and without label", size="sm", show_close_button=True, show_label=False)
            with gr.Row():
                Banner(label="Custom label and icon", value="Large info banner with custom icon", icon="https://i.pinimg.com/originals/e9/ab/30/e9ab30fdcadf40bdc095a1e317f3851c.gif")
        with gr.Column():
            Banner(value="Large success banner with specified value", variant="success")

if __name__ == "__main__":
    demo.launch()

```

## Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>variant</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"info"</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>icon</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>size</code></td>
<td align="left" style="width: 25%;">

```python
Literal["sm", "lg"] | None
```

</td>
<td align="left"><code>"lg"</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>show_close_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>show_icon</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
Component | list[Component] | set[Component] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left"></td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left"></td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the Banner changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the Banner. |
| `submit` | This listener is triggered when the user presses the Enter key while the Banner is focused. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes text value as a {str} into the function.
- **As input:** Should return, expects a {str} returned from function and sets textarea value to it.

 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 
