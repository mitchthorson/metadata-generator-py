##metadata-generator

I've gotten tired of wrangling all the HTML meta properties into the necessary tags such as:
```html
<meta name="description" content="description" />
<meta property="og:description" content="description"/>
<meta name="twitter:description" content="description">
<meta property="og:type" content="website">
<meta name="twitter:title" content="title">
<meta property="og:title" content="title"/>
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="http://www.example.com">
<meta property="og:image" content="http://www.example.com/images/image.jpg">
<meta name="twitter:image" content="http://www.example.com/images/image.jpg">
 ```

 Too much copying and pasting. This python package is a solution to all the duplication. Simply run 
 ```
 metadata-generator
 ```
 and specify the title, description, url, and image properties just once and viola, metadata.

 This probably isn't very useful for you. Your fancy CMS probably does this for you. But if like me, you're on your own, this might be useful.

##Installation

To use this package, run

```
pip install git+git://github.com/mitchthorson/metadata-generator-py/
```

and you're good to go.

##Development
If you want to make changes, (maybe more meta tags??) just pull down the code and hack away. Currently there are no external dependencies. If that ever changes, I'd reccomend setting up a virtual environment.


