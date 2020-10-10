const darkThemeSelected =
    ((localStorage.getItem('darkSwitch') === null) &&
        (window.matchMedia('(prefers-color-scheme: dark)').matches === true)) ||
    localStorage.getItem('darkSwitch') === 'dark';
darkThemeSelected ? document.body.setAttribute('data-theme', 'dark') :
    document.body.removeAttribute('data-theme');
