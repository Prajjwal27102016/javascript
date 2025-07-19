const body = document.querySelector('body');
const button = document.querySelector('button');
const colors = [
  'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'magenta', 'lime',
  'teal', 'brown', 'gray', 'black', 'white', 'gold', 'silver', 'coral', 'navy', 'olive',
  'maroon', 'indigo', 'violet', 'turquoise', 'salmon', 'plum', 'khaki', 'tan', 'peach',
  'lavender', 'mint', 'beige', 'aqua', 'fuchsia', 'orchid', 'peru', 'sienna', 'steelblue',
  'lightcoral', 'lightsalmon', 'lightseagreen', 'lightsteelblue', 'lightyellow', 'lightgreen',
  'lightpink', 'lightskyblue', 'lightgray', 'lightgoldenrodyellow', 'lightcyan', 'lightblue',
  'lightpurple', 'lightorange', 'lightlime', 'lightmagenta', 'lightteal', 'lightbrown',
  'lightindigo', 'lightviolet', 'lightturquoise', 'lightcoral', 'lightnavy', 'lightolive',
  'lightmaroon', 'lightplum', 'lightkhaki', 'lighttan', 'lightpeach', 'lightlavender',
  'lightmint', 'lightbeige', 'lightaqua', 'lightfuchsia', 'lightorchid', 'lightperu',
  'lightsienna', 'lightsteelblue', 'lightlightcoral', 'lightlightsalmon', 'lightlightseagreen',
];

body.style.backgroundColor = 'white';
button.addEventListener('click', function() {
    const colorIndex = Math.floor(Math.random() * colors.length);
    body.style.backgroundColor = colors[colorIndex];
});