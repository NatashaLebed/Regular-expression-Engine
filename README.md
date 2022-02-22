# Regular-expression-Engine
JetBrain study project

### Compares regular expression with a string and determines if there's a match.

`.` match any character in the target string.

`^` can occur at the beginning of the regex, and it means that the following regex should be matched only at the beginning of the input string.

`$` can occur at the end of the regex, and it means that the preceding regex should be matched only at the end of the input string.

#### Examples
| Input                            | Output      |
| -------------------------------- | ----------- |
|Input:    '^app\|apple'           |Output: True |  
|Input:     'le$\|apple'           |Output: True | 
|Input:      '^a\|apple'           |Output: True | 
|Input:      '.$\|apple'           |Output: True | 
|Input:  'apple$\|tasty apple'     |Output: True | 
|Input:  '^apple\|apple pie'       |Output: True | 
|Input: '^apple$\|apple'           |Output: True | 
|Input: '^apple$\|tasty apple'     |Output: False|   
|Input: '^apple$\|apple pie'       |Output: False|  
|Input:    'app$\|apple'           |Output: False|   
|Input:     '^le\|apple'           |Output: False|  

`?` matches the preceding character zero times or once;  
`*` matches the preceding character zero or more times;  
`+` matches the preceding character once or more times.  
`\` if a metacharacter is preceded by a backward slash, it is considered as a normal literal and can be matched.

#### Examples
| Input                            | Output      |
| -------------------------------- | ----------- |
|Input: 'colou?r\|color'       |Output: True  |
|Input: 'colou?r\|colour'      |Output: True  |
|Input: 'colou?r\|colouur'     |Output: False | 
|Input: 'colou*r\|color'       |Output: True  |
|Input: 'colou*r\|colour'      |Output: True  |
|Input: 'colou*r\|colouur'     |Output: True  |
|Input:  'col.*r\|color'       |Output: True  |
|Input:  'col.*r\|colour'      |Output: True  |
|Input:  'col.*r\|colr'        |Output: True | 
|Input:  'col.*r\|collar'      |Output: True  |

| Input                            | Output      |
| -------------------------------- | ----------- |
|Input:  '\\.$\|end.'              |True  |
|Input:  '3\\+3\|3+3=6'            |True | 
|Input:  '\\?\|Is this working?'   |True | 
|Input:  '\\\\\|\\'                  |True |
|Input: 'colou\\?r\|color'         |False | 
|Input: 'colou\\?r\|colour'        |False  |
|Input: 'col.*r$\|colors'         |False  |

