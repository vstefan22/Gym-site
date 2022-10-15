

function initMap() {
// The location of Uluru
const uluru = { lat: 44.765847893455806, lng: 17.207241303074138 };
// The map, centered at Uluru
const map = new google.maps.Map(document.getElementById("map"), {
zoom: 10,
center: uluru,
});
// The marker, positioned at Uluru
const marker = new google.maps.Marker({
position: uluru,
map: map,
});
}

window.initMap = initMap;


const swiper = new Swiper('.swiper', {
    // Optional parameters
    autoplay: {
        delay: 3000,
        dusableOnInteraction: false,
    },
    direction: 'horizontal',
    loop: true,

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});
 