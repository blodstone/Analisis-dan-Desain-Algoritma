def naive_justify(text, page_size):
    next = text.get_next()
    total_size = 0
    next_total_size = total_size + next.size()

    lines = [[next]]
    current_line = 0

    while(!text.empty()):
        while(next_total_size < page_size):
            total_size = next_total_size
            next = text.get_next()
            lines[current_line].push(next)
            next_total_size = total_size + next.size()

        while total_size != page_size:
            add_space(lines[current_line])

        current_line = current_line + 1

