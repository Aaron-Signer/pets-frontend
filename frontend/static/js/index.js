// TODO: Need to figure out why import assertions are failing

// import * as animalMappia
// const piexif = require('piexifjs');

// main.mjs
// import('./animal_mapping.json', {
//     assert: { type: 'json' }
//   }).then((res) => {
//     console.log(res);
//   });

// const jsonModule = await import('/json/animal_mapping.json', {
// assert: { type: 'json' }
// });
// console.log(jsonModule.default.answer);

const response = await fetch('/json/animal_mapping.json');
const data = await response.json();
const imageKeys = Object.keys(data)
let numberOfColumns = 4;

const pictureWidth = (window.innerWidth - 96 )/numberOfColumns;

for(let i = 0; i < imageKeys.length; i++) {
    if ('content' in document.createElement('template')) {
        const key = imageKeys[i];
        let image = data[key];
        const selector = "#animal_image_panes_" + (i%numberOfColumns + 1);
        const animalImagePanes = document.querySelector(selector);

        const animalImageTemplate = document.querySelector('#animal_image_template');

        const clone = animalImageTemplate.content.cloneNode(true);
        let td = clone.querySelector("div");

        var img = new Image();
        img.width = pictureWidth;
        img.src = image.urlPath;
        img.classList.add("general-image");

        td.appendChild(img);

        animalImagePanes.appendChild(img);
        console.log(animalImagePanes.clientHeight)
    }
}