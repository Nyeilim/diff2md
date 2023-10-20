# Introduce
Find the differences between two texts and output the corrected text with Markdown

The code is used for correcting my dictation of English listening materials. So there's some special feature between the sample text and dictation(origin) text.
1. Two texts will have the same number of lines.
2. The text maybe lacks a lot. Forgive my poor English~ 😂
3. The text usually contains multiple lines and split with '\n\n'.

And the program will do some preprocessing to the text for ignoring some unimportant mistake.
1. Ignore case. That means 'The' and 'the' will be recognized the same text.
2. Ignore punctuation. That means 'day.' and 'day' will be recognized the same text.

# The effects of text correction
## Origin Text
To prepare  send astronauts to Mars, NASA began taking application Friday for 4 people to live a year in Mars

1300 suqare feet insde a building in Huston.

The paid volunteers will work in a environment smiliar to Mars.

They will have limited communications with family, restricted food and resources.

NASA is planning three experiments with first one starting in the four next year.

Food will all ready to eat, space food.

Some plants will be growth but not potato liking the movie "The Mars".

We want to understand how human perform in them. Said lead scienctists. we looking at mars realistic situation.

The application process open Friday and then not seeking just anybody.

The requirements are strict, including a master degree of science, engeering, math field or pilot experience.

Only American citizens or permanent US residents are acceptable.

applicants must be between 30 and 55, and in good physical health.

Altitude is key, said former canadian astronaut, 

He said the participants need to be super competent, resourceful, and not rely on other people to feel comfortable.

---
## Sample Text
To prepare for eventually sending astronauts to Mars, NASA began taking applications Friday for four people to live for a year in Mars Dune Alpha.

That's a 1,700-square-foot Martian habitat inside a building in Houston.

The paid volunteers will work in environment similar to Mars.

They will have limited communications with family, restricted food and resources.

NASA is planning three experiments with the first one starting in the fall next year.

Food will all be ready-to-eat space food.

Some plants will be grown, but not potatoes like in the movie "The Martian".

"We want to understand how humans perform in them," said lead scientist Grace Douglas. "We're looking at Mars realistic situations."

The application process opened Friday and they're not seeking just anybody.

The requirements are strict, including a master's degree in a science, engineering or math field or pilot experience.

Only American citizens or permanent U.S. residents are acceptable.

Applicants must be between 30 and 55 and in good physical health.

"Attitude is key," said former Canadian astronaut Chris Hadfield.

He said the participants need to be super competent, resourceful, and not rely on other people to feel comfortable.

---
## Corrected Text
To prepare ~~send~~ ==for eventually sending== astronauts to Mars, NASA began taking ~~application~~ ==applications== Friday for ~~4~~ ==four== people to live ==for== a year in Mars ==Dune Alpha.==

~~1300 suqare feet insde~~ ==That's a 1,700-square-foot Martian habitat inside== a building in ~~Huston.~~ ==Houston.==

The paid volunteers will work in ~~a~~ environment ~~smiliar~~ ==similar== to Mars.

They will have limited communications with family, restricted food and resources.

NASA is planning three experiments with ==the== first one starting in the ~~four~~ ==fall== next year.

Food will all ~~ready to eat,~~ ==be ready-to-eat== space food.

Some plants will be ~~growth~~ ==grown,== but not ~~potato liking~~ ==potatoes like in== the movie "The ~~Mars".~~ ==Martian".==

"We want to understand how ~~human~~ ==humans== perform in them," said lead ~~scienctists. we~~ ==scientist Grace Douglas. "We're== looking at Mars realistic ~~situation.~~ ==situations."==

The application process ~~open~~ ==opened== Friday and ~~then~~ ==they're== not seeking just anybody.

The requirements are strict, including a ~~master~~ ==master's== degree ~~of~~ ==in a== science, ~~engeering,~~ ==engineering or== math field or pilot experience.

Only American citizens or permanent U.S. residents are acceptable.

Applicants must be between 30 and 55 and in good physical health.

~~Altitude~~ =="Attitude== is key," said former Canadian astronaut ==Chris Hadfield.==

He said the participants need to be super competent, resourceful, and not rely on other people to feel comfortable.

---
## Corrected Text Rendered in Siyuan
![](https://raw.githubusercontent.com/Nyeilim/image-hosting/main/share/202310201636924.png)
