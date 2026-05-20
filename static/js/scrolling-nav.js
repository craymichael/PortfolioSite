// Smooth in-page anchor scrolling. Native scrollIntoView, no jQuery Easing.
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a.page-scroll').forEach(function (a) {
        a.addEventListener('click', function (e) {
            var href = a.getAttribute('href');
            if (!href || href.charAt(0) !== '#') return;
            var target = document.querySelector(href);
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({behavior: 'smooth', block: 'start'});
        });
    });
});
