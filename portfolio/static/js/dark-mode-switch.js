/**
 * MIT License

 Copyright (c) 2019 Christian Oliff
 2020 Zach Carmichael (modified)

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
 */
const darkSwitch = document.getElementById('darkSwitch');
window.addEventListener('load', () => {
    if (darkSwitch) {
        initTheme();
        darkSwitch.addEventListener('change', () => {
            resetTheme();
        });
    }
});

/**
 * Set of elements that should have the `data-theme` tag added, if needed.
 * Ex: recaptcha
 */
const darkModeElements = new Set([document.body]);

/**
 * Summary: function that adds or removes the attribute 'data-theme' depending if
 * the switch is 'on' or 'off'.
 *
 * Description: initTheme is a function that uses localStorage from JavaScript DOM,
 * to store the value of the HTML switch. If the switch was already switched to
 * 'on' it will set an HTML attribute to the body named: 'data-theme' to a 'dark'
 * value. If it is the first time opening the page, or if the switch was off the
 * 'data-theme' attribute will not be set.
 * @return {void}
 */
function initTheme() {
    const darkThemeSelected =
        ((localStorage.getItem('darkSwitch') === null) &&
            (window.matchMedia('(prefers-color-scheme: dark)').matches === true)) ||
        localStorage.getItem('darkSwitch') === 'dark';
    darkSwitch.checked = darkThemeSelected;
    darkThemeSelected ? darkModeElements.forEach(function (el) {
        el.setAttribute('data-theme', 'dark')
    }) : darkModeElements.forEach(function (el) {
        el.removeAttribute('data-theme')
    });
}


/**
 * Summary: resetTheme checks if the switch is 'on' or 'off' and if it is toggled
 * on it will set the HTML attribute 'data-theme' to dark so the dark-theme CSS is
 * applied.
 * @return {void}
 */
function resetTheme() {
    if (darkSwitch.checked) {
        darkModeElements.forEach(function (el) {
            el.setAttribute('data-theme', 'dark')
        })
        localStorage.setItem('darkSwitch', 'dark');
    } else {
        darkModeElements.forEach(function (el) {
            el.removeAttribute('data-theme')
        });
        localStorage.removeItem('darkSwitch');
    }
}

function addDarkModeElement(el) {
    darkModeElements.add(el);
    resetTheme();
}