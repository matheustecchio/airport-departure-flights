function adjustIframeHeight(iframe) {
    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
}

window.addEventListener("message", function(event) {
    const iframe = document.querySelector('iframe');
    iframe.style.height = event.data + 'px';
});
