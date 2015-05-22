def generate_lesson_HTML(lesson_title, concept_description):
	html_text_1 = '''
<div class = "lesson">
	<div class = "lesson-title">
		''' + lesson_title
	html_text_2 = '''
	</div>
	<div class = "concept_description">
		''' + concept_description
	html_text_3 = '''
	</div>
</div>'''

	full_html_text = html_text_1 + html_text_2 + html_text_3
	return full_html_text
		
def get_title(lesson):
	start_location = lesson.find('TITLE:')
	end_location = lesson.find('DESCRIPTION:')
	title = lesson[start_location+7 :end_location-1]
	return title
	
def get_description(lesson):
	start_location = lesson.find('DESCRIPTION:')
	description = lesson[start_location+13 :]
	return description
	
def get_lesson_by_number(text, lesson_number):
	counter = 0
	while counter < lesson_number:
		counter = counter + 1
		next_lesson_start = text.find('TITLE:')
		next_lesson_end = text.find('TITLE:', next_lesson_start + 1)
		lesson = text[next_lesson_start:next_lesson_end]
		text = text[next_lesson_end:]
	return lesson			

TEST_TEXT = """TITLE: What We Will Do
DESCRIPTION: The programs we write will be Python code which we will input into 
another program which is a Python interpreter that follows the instructions in our code.
TITLE: Terms to Know
DESCRIPTION: "Web Crawler" collects data from the web. "Computer" is a machine that can
do everything; however, it can't do anything without a program.
TITLE: Python Expressions
DESCRIPTION: An "expression" is something that has a value. The "expression" non-terminal
is on the left and can be replaced by an "expression", followed by an "operator", followed
by another "expression"."""


def generate_all_html(text):
	current_lesson_number = 1
	lesson = get_lesson_by_number(text, current_lesson_number)
	all_html = ''
	while lesson != '':
		title = get_title(lesson)
		description = get_description(lesson)
		lesson_html = generate_lesson_HTML(title, description)
		all_html = all_html + lesson_html
		current_lesson_number = current_lesson_number + 1
		lesson = get_lesson_by_number(text, current_lesson_number)
	return all_html
	
print generate_all_html(TEST_TEXT)		

														