_DEBUG = True

w, h = 800, 800

# Where the code starts and ends (y)
code_start = h/60
code_end = h - code_start
# Indent values
indent_size = int(h/24)
max_indents = 6
indent_inc_chance = .4
indent_dec_chance = .3
if _DEBUG:
    indent_inc_chance = 0
    indent_dec_chance = 0

# Code Segments (Number and length)
min_segments = 2
max_segments = 16
if _DEBUG:
    min_segments = max_segments
segment_sep = int(w / 60)
min_segment_length = int(w / 160)
row_len_fact = 1.0 # 0.0 < row_len_fact <= 1.0
row_len = int(row_len_fact * (w - (indent_size*2)) + segment_sep ) # length of line (row)
max_segment_length = int(row_len / max_segments - segment_sep)
if _DEBUG:
    min_segment_length = max_segment_length #DEBUG

# Lines of code
min_code_lines = 8
#max_code_lines = h / 2
max_code_lines = h / 5
if _DEBUG:
    min_code_lines = 2
    max_code_lines = 40
code_lines = int(random(min_code_lines,max_code_lines))
#code_lines = 2
#code_lines = 3
#code_lines = 4
#code_lines = 8
#code_lines = 25
#code_lines = 80
#code_lines = 400

code_sep = (code_end - code_start)/(code_lines - 1.0) 

# Code Line Thickness (must be < code_sep)
#code_size = int(w / 120) 
code_size = code_sep / 1.5
max_code_size = ceil(h / 80.0)
if (code_size > max_code_size):
    code_size = max_code_size
#print(code_size)

line_break_chance = .4
if _DEBUG:
    line_break_chance = 0.0
    #line_break_chance = 0.1

# Random Colors
random_colors = False

# Higher value means the color will change more often
#change_chance = .4
change_chance = .6

# If you want to use your own color palette, just set random colors to false
#colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]
colors = [(92,97,130), (79,164,165), (202,166,122), (212,117,100)]

# Background Color
bc = (30, 30, 30)

def set_random_color():
    stroke(random(50, 200), random(50, 200), random(50, 200))

def set_palette_color():
    c = colors[int(random(len(colors)))]
    stroke(c[0], c[1], c[2])


def setup():
    # Take advantage of resolution
    pixelDensity(2)

    # Setting the size and background
    size(w, h)
    background(bc[0], bc[1], bc[2])

    # Type of lines and size
    strokeCap(ROUND)
    strokeWeight(code_size)

    if (random_colors == True):
        set_random_color()
    else:
        set_palette_color()

    line_y = code_start
    indent = 0
    for i in range(code_lines):
        #if (i < 4):
        #     stroke(*colors[i])
        if (not (random(1) < line_break_chance and indent is 0)):
            line_x = indent_size + (indent * indent_size)
            line_segments = int(random(min_segments, max_segments))
            for j in range(line_segments):
                if (random(1) < change_chance):
                    if random_colors:
                        set_random_color()
                    else:
                        set_palette_color()
                segment_length = random(min_segment_length, max_segment_length)

                line(line_x, line_y, line_x + segment_length, line_y)

                line_x = line_x + segment_length + segment_sep
            if (random(1) < indent_inc_chance and indent < max_indents):
                indent += 1
            elif(random(1) < indent_dec_chance and indent > 0):
                indent -= int(random(1, max_indents))
                if (indent < 0):
                    indent = 0
        print("i={} code_start={} code_end={} code_size={} code_sep={} line_y={}".format(i,code_start,code_end,code_size,code_sep,line_y))
        line_y += code_sep

    print(code_sep * code_lines)
    print(code_sep * code_lines + code_start + h - code_end)

        #seed = int(random(10000))
    save('Examples/Reddit.png')
    #print(seed)
