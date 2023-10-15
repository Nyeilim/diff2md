def next_step(component):
    comp = component
    comp.origin_text = comp.text_box.get("1.0", "end-1c")  # get text from start to end
    comp.text_box.delete("1.0", "end")  # clear text box
    comp.text_box.insert("1.0", "请输入范文...")  # fill text box
    comp.next_button.grid_remove()
    comp.process_button.grid()  # appear the hidden button


def process_text(component):
    comp = component
    sample_text = comp.text_box.get("1.0", "end-1c")  # get text from start to end
    corrected_text = comp.origin_text + "这里是处理结果..."
    comp.text_box.delete("1.0", "end")
    comp.text_box.insert("1.0", corrected_text)
    comp.process_button.grid_remove()
