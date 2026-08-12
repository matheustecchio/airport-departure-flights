function getValidIframeHeight(value) {
    const height = typeof value === "number" ? value : Number(value);

    if (!Number.isFinite(height) || height <= 0 || height > 100000) {
        return null;
    }

    return Math.ceil(height);
}

function setMeasuredIframeHeight(iframe, iframeDocument) {
    const height = getValidIframeHeight(Math.max(
        iframeDocument?.body?.scrollHeight || 0,
        iframeDocument?.documentElement?.scrollHeight || 0
    ));

    if (height !== null) {
        iframe.style.height = `${height}px`;
    }
}

function revealStyledIframe(iframe, iframeDocument) {
    iframe.classList.add("is-ready");
    setMeasuredIframeHeight(iframe, iframeDocument);
}

function setIframeAvailability(iframe, isAvailable) {
    const frame = iframe.closest(".iframe-frame");

    if (!frame) {
        return;
    }

    const existingEmptyState = frame.querySelector(".data-empty");
    frame.classList.toggle("is-unavailable", !isAvailable);
    iframe.hidden = !isAvailable;

    if (isAvailable) {
        existingEmptyState?.remove();
        return;
    }

    if (existingEmptyState) {
        return;
    }

    const emptyState = document.createElement("div");
    const title = document.createElement("strong");
    const guidance = document.createElement("span");

    emptyState.className = "data-empty";
    emptyState.setAttribute("role", "status");
    title.textContent = "Generated data is not available.";
    guidance.textContent = "Install requirements, then run python3 cmd/main.py to create the latest departure tables.";
    emptyState.append(title, guidance);
    frame.appendChild(emptyState);
}

function applyIframeStyles(iframe, iframeDocument) {
    if (!iframeDocument?.head) {
        setIframeAvailability(iframe, false);
        return;
    }

    iframeDocument.documentElement.classList.add("embedded-data");

    const existingStylesheet = iframeDocument.getElementById("airport-dashboard-styles");

    if (existingStylesheet) {
        if (existingStylesheet.sheet) {
            revealStyledIframe(iframe, iframeDocument);
        } else {
            setIframeAvailability(iframe, false);
        }
        return;
    }

    const stylesheet = iframeDocument.createElement("link");
    stylesheet.id = "airport-dashboard-styles";
    stylesheet.rel = "stylesheet";
    stylesheet.href = new URL("style.css", window.location.href).href;
    stylesheet.addEventListener("load", function () {
        revealStyledIframe(iframe, iframeDocument);
    });
    stylesheet.addEventListener("error", function () {
        setIframeAvailability(iframe, false);
    });
    iframeDocument.head.appendChild(stylesheet);
}

function adjustIframeHeight(iframe) {
    if (!(iframe instanceof HTMLIFrameElement)) {
        return;
    }

    try {
        const iframeDocument = iframe.contentDocument || iframe.contentWindow?.document;

        if (!iframeDocument?.querySelector("table.dataframe")) {
            setIframeAvailability(iframe, false);
            return;
        }

        setIframeAvailability(iframe, true);
        applyIframeStyles(iframe, iframeDocument);
    } catch (_error) {
        setIframeAvailability(iframe, false);
    }
}

window.addEventListener("message", function (event) {
    const height = getValidIframeHeight(event.data);

    if (height === null) {
        return;
    }

    const sourceIframe = Array.from(document.querySelectorAll("iframe")).find(
        (iframe) => iframe.contentWindow === event.source
    );

    if (sourceIframe) {
        sourceIframe.style.height = `${height}px`;
    }
});
