(function(doc, win) {
    const hashRe = /^#/;
    doc.addEventListener("click", (e) => {
        let href = e.target.hash;
        console.log(href);
        if (href && hashRe.exec(href)) {
            e.preventDefault();
            doc.querySelector(href).scrollIntoView({behavior: 'smooth'});
        }
    }, true);
}(document, window));
