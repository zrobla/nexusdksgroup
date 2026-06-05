document.addEventListener("DOMContentLoaded", function () {
    var body = document.body;
    var header = document.querySelector(".site-header");
    var navToggle = document.querySelector(".menu-toggle");
    var navLinks = document.querySelectorAll(".site-nav a.nav-link, .site-nav .nav-dropdown-link, .site-nav .lang-link");
    var navDropdowns = document.querySelectorAll(".nav-dropdown");
    var contactForm = document.querySelector("#contact-brief");
    var desktopNav = window.matchMedia("(min-width: 992px)");

    var closeNavDropdown = function (dropdown) {
        var toggle = dropdown ? dropdown.querySelector(".nav-dropdown-toggle") : null;
        if (!dropdown || !toggle) {
            return;
        }

        dropdown.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
    };

    var closeAllNavDropdowns = function (exceptDropdown) {
        navDropdowns.forEach(function (dropdown) {
            if (dropdown !== exceptDropdown) {
                closeNavDropdown(dropdown);
            }
        });
    };

    var syncHeaderState = function () {
        if (!header) {
            return;
        }

        if (window.scrollY > 24) {
            header.classList.add("is-scrolled");
        } else {
            header.classList.remove("is-scrolled");
        }
    };

    if (header) {
        syncHeaderState();
        window.addEventListener("scroll", syncHeaderState, { passive: true });
    }

    if (navToggle && header) {
        navToggle.addEventListener("click", function () {
            var isOpen = header.classList.toggle("is-open");
            body.classList.toggle("nav-open", isOpen);
            navToggle.setAttribute("aria-expanded", String(isOpen));

            if (!isOpen) {
                closeAllNavDropdowns();
            }
        });

        navLinks.forEach(function (link) {
            link.addEventListener("click", function () {
                header.classList.remove("is-open");
                body.classList.remove("nav-open");
                navToggle.setAttribute("aria-expanded", "false");
                closeAllNavDropdowns();
            });
        });
    }

    if (navDropdowns.length) {
        navDropdowns.forEach(function (dropdown) {
            var toggle = dropdown.querySelector(".nav-dropdown-toggle");
            var closeTimer = 0;

            var clearCloseTimer = function () {
                if (!closeTimer) {
                    return;
                }

                window.clearTimeout(closeTimer);
                closeTimer = 0;
            };

            var openDropdown = function () {
                clearCloseTimer();
                closeAllNavDropdowns(dropdown);
                dropdown.classList.add("is-open");
                toggle.setAttribute("aria-expanded", "true");
            };

            var scheduleClose = function () {
                clearCloseTimer();
                closeTimer = window.setTimeout(function () {
                    closeNavDropdown(dropdown);
                    closeTimer = 0;
                }, 180);
            };

            if (!toggle) {
                return;
            }

            toggle.addEventListener("click", function (event) {
                event.preventDefault();

                var isOpen = dropdown.classList.contains("is-open");
                clearCloseTimer();

                if (isOpen) {
                    closeNavDropdown(dropdown);
                } else {
                    openDropdown();
                }
            });

            dropdown.addEventListener("keydown", function (event) {
                if (event.key === "Escape") {
                    clearCloseTimer();
                    closeNavDropdown(dropdown);
                    toggle.focus();
                }
            });

            dropdown.addEventListener("mouseenter", function () {
                if (!desktopNav.matches) {
                    return;
                }

                openDropdown();
            });

            dropdown.addEventListener("mouseleave", function () {
                if (!desktopNav.matches) {
                    return;
                }

                scheduleClose();
            });
        });

        document.addEventListener("click", function (event) {
            navDropdowns.forEach(function (dropdown) {
                if (!dropdown.contains(event.target)) {
                    closeNavDropdown(dropdown);
                }
            });
        });
    }

    var revealItems = document.querySelectorAll(".reveal");
    if (revealItems.length) {
        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.18 });

        revealItems.forEach(function (item) {
            revealObserver.observe(item);
        });
    }

    var tabButtons = document.querySelectorAll("[data-tab-set][data-tab-target]");
    tabButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var set = button.getAttribute("data-tab-set");
            var target = button.getAttribute("data-tab-target");
            var setButtons = document.querySelectorAll("[data-tab-set='" + set + "'][data-tab-target]");
            var panels = document.querySelectorAll("[data-tab-set='" + set + "'][data-tab-panel]");

            setButtons.forEach(function (item) {
                item.classList.toggle("is-active", item === button);
            });

            panels.forEach(function (panel) {
                var isMatch = panel.getAttribute("data-tab-panel") === target;
                panel.hidden = !isMatch;
            });
        });
    });

    var filterButtons = document.querySelectorAll("[data-filter-set][data-filter]");
    filterButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var set = button.getAttribute("data-filter-set");
            var target = button.getAttribute("data-filter");
            var setButtons = document.querySelectorAll("[data-filter-set='" + set + "'][data-filter]");
            var cards = document.querySelectorAll("[data-filter-set='" + set + "'][data-category]");

            setButtons.forEach(function (item) {
                item.classList.toggle("is-active", item === button);
            });

            cards.forEach(function (card) {
                var categories = (card.getAttribute("data-category") || "").split(" ");
                var isVisible = target === "all" || categories.indexOf(target) !== -1;
                card.classList.toggle("is-hidden", !isVisible);
            });
        });
    });

    var accordionTriggers = document.querySelectorAll("[data-accordion-trigger]");
    accordionTriggers.forEach(function (trigger) {
        trigger.addEventListener("click", function () {
            var panelId = trigger.getAttribute("aria-controls");
            var panel = panelId ? document.getElementById(panelId) : null;
            var isExpanded = trigger.getAttribute("aria-expanded") === "true";

            trigger.setAttribute("aria-expanded", String(!isExpanded));
            if (panel) {
                panel.hidden = isExpanded;
            }
        });
    });

    var heroSection = document.querySelector(".hero-slider");
    if (heroSection) {
        var heroSlides = heroSection.querySelectorAll(".hero-slide");
        var heroCopySlides = heroSection.querySelectorAll(".hero-copy-slide");
        var heroDots = heroSection.querySelectorAll("[data-hero-dot]");
        var heroPrev = heroSection.querySelector("[data-hero-prev]");
        var heroNext = heroSection.querySelector("[data-hero-next]");
        var heroIndex = 0;
        var heroTimer = null;

        var syncHero = function (index) {
            heroSlides.forEach(function (slide, slideIndex) {
                var isActive = slideIndex === index;
                slide.classList.toggle("is-active", isActive);
                slide.setAttribute("aria-hidden", String(!isActive));
            });

            heroCopySlides.forEach(function (slide, slideIndex) {
                var isActive = slideIndex === index;
                slide.classList.toggle("is-active", isActive);
                slide.setAttribute("aria-hidden", String(!isActive));
            });

            heroDots.forEach(function (dot, dotIndex) {
                var isActive = dotIndex === index;
                dot.classList.toggle("is-active", isActive);
                dot.setAttribute("aria-current", String(isActive));
            });
        };

        var goHero = function (nextIndex) {
            heroIndex = (nextIndex + heroSlides.length) % heroSlides.length;
            syncHero(heroIndex);
        };

        var stopHeroAuto = function () {
            if (heroTimer) {
                window.clearInterval(heroTimer);
                heroTimer = null;
            }
        };

        var startHeroAuto = function () {
            stopHeroAuto();
            heroTimer = window.setInterval(function () {
                goHero(heroIndex + 1);
            }, 6800);
        };

        if (heroSlides.length) {
            syncHero(heroIndex);

            if (heroPrev) {
                heroPrev.addEventListener("click", function () {
                    goHero(heroIndex - 1);
                    startHeroAuto();
                });
            }

            if (heroNext) {
                heroNext.addEventListener("click", function () {
                    goHero(heroIndex + 1);
                    startHeroAuto();
                });
            }

            heroDots.forEach(function (dot, dotIndex) {
                dot.addEventListener("click", function () {
                    goHero(dotIndex);
                    startHeroAuto();
                });
            });

            startHeroAuto();
            heroSection.addEventListener("mouseenter", stopHeroAuto);
            heroSection.addEventListener("mouseleave", startHeroAuto);
            heroSection.addEventListener("focusin", stopHeroAuto);
            heroSection.addEventListener("focusout", startHeroAuto);
        }
    }

    // Slider du hero NEXUS : diapos entières (.nx-hero-slide) avec puces + flèches.
    var nxHero = document.querySelector(".nx-hero-slider");
    if (nxHero) {
        var nxSlides = nxHero.querySelectorAll("[data-hero-slide]");
        var nxDots = nxHero.querySelectorAll("[data-hero-dot]");
        var nxPrev = nxHero.querySelector("[data-hero-prev]");
        var nxNext = nxHero.querySelector("[data-hero-next]");
        var nxIndex = 0;
        var nxTimer = null;
        var nxReduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

        var nxSync = function (index) {
            nxSlides.forEach(function (slide, i) {
                var on = i === index;
                slide.classList.toggle("is-active", on);
                slide.setAttribute("aria-hidden", String(!on));
            });
            nxDots.forEach(function (dot, i) {
                var on = i === index;
                dot.classList.toggle("is-active", on);
                dot.setAttribute("aria-current", String(on));
            });
        };

        var nxGo = function (next) {
            nxIndex = (next + nxSlides.length) % nxSlides.length;
            nxSync(nxIndex);
        };

        var nxStop = function () {
            if (nxTimer) { window.clearInterval(nxTimer); nxTimer = null; }
        };

        var nxStart = function () {
            nxStop();
            if (nxReduce || nxSlides.length < 2) { return; }
            nxTimer = window.setInterval(function () { nxGo(nxIndex + 1); }, 6500);
        };

        if (nxSlides.length) {
            nxSync(nxIndex);

            if (nxPrev) {
                nxPrev.addEventListener("click", function () { nxGo(nxIndex - 1); nxStart(); });
            }
            if (nxNext) {
                nxNext.addEventListener("click", function () { nxGo(nxIndex + 1); nxStart(); });
            }
            nxDots.forEach(function (dot, i) {
                dot.addEventListener("click", function () { nxGo(i); nxStart(); });
            });

            nxStart();
            nxHero.addEventListener("mouseenter", nxStop);
            nxHero.addEventListener("mouseleave", nxStart);
            nxHero.addEventListener("focusin", nxStop);
            nxHero.addEventListener("focusout", nxStart);
        }
    }

    var carousels = document.querySelectorAll("[data-carousel]");
    carousels.forEach(function (carousel) {
        var track = carousel.querySelector("[data-carousel-track]");
        var prev = carousel.querySelector("[data-carousel-prev]");
        var next = carousel.querySelector("[data-carousel-next]");
        var autoTimer = null;

        if (!track) {
            return;
        }

        var getStep = function () {
            var firstSlide = track.querySelector(".carousel-slide");
            var gap = parseFloat(window.getComputedStyle(track).gap || "0");

            if (!firstSlide) {
                return track.clientWidth * 0.84;
            }

            return firstSlide.getBoundingClientRect().width + gap;
        };

        var moveTrack = function (direction) {
            track.scrollBy({
                left: direction * getStep(),
                behavior: "smooth",
            });
        };

        if (prev) {
            prev.addEventListener("click", function () {
                moveTrack(-1);
            });
        }

        if (next) {
            next.addEventListener("click", function () {
                moveTrack(1);
            });
        }

        if (carousel.hasAttribute("data-carousel-autoplay")) {
            var stopAuto = function () {
                if (autoTimer) {
                    window.clearInterval(autoTimer);
                    autoTimer = null;
                }
            };

            var startAuto = function () {
                stopAuto();
                autoTimer = window.setInterval(function () {
                    var limit = track.scrollWidth - track.clientWidth - 8;
                    if (track.scrollLeft >= limit) {
                        track.scrollTo({ left: 0, behavior: "smooth" });
                    } else {
                        moveTrack(1);
                    }
                }, 3600);
            };

            startAuto();
            carousel.addEventListener("mouseenter", stopAuto);
            carousel.addEventListener("mouseleave", startAuto);
            carousel.addEventListener("focusin", stopAuto);
            carousel.addEventListener("focusout", startAuto);
        }
    });

    var partnerRails = document.querySelectorAll("[data-partners-carousel]");
    if (partnerRails.length) {
        var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

        partnerRails.forEach(function (rail) {
            if (rail.getAttribute("data-carousel-ready") === "true") {
                return;
            }

            var cards = Array.prototype.slice.call(rail.children);
            if (cards.length < 2) {
                return;
            }

            cards.forEach(function (card) {
                var clone = card.cloneNode(true);
                clone.setAttribute("aria-hidden", "true");
                rail.appendChild(clone);
            });

            rail.setAttribute("data-carousel-ready", "true");
            rail.scrollLeft = 0;

            var timerId = 0;
            var isPointerDown = false;
            var startX = 0;
            var startScrollLeft = 0;
            var lastTs = 0;
            var speedPxPerSecond = reducedMotion.matches ? 22 : 66;

            var stepRail = function () {
                var timestamp = Date.now();
                if (!lastTs) {
                    lastTs = timestamp;
                }

                var dt = Math.min(64, timestamp - lastTs);
                lastTs = timestamp;

                if (!isPointerDown) {
                    rail.scrollLeft += speedPxPerSecond * dt / 1000;

                    if (rail.scrollLeft >= rail.scrollWidth / 2) {
                        rail.scrollLeft = 0;
                    }
                }
            };

            var startRail = function () {
                if (timerId) {
                    return;
                }

                lastTs = Date.now();
                timerId = window.setInterval(stepRail, 24);
            };

            var stopRail = function () {
                if (!timerId) {
                    return;
                }

                window.clearInterval(timerId);
                timerId = 0;
            };

            var onPointerDown = function (event) {
                isPointerDown = true;
                startX = event.clientX;
                startScrollLeft = rail.scrollLeft;
                rail.classList.add("is-dragging");

                if (typeof rail.setPointerCapture === "function") {
                    rail.setPointerCapture(event.pointerId);
                }
            };

            var onPointerMove = function (event) {
                if (!isPointerDown) {
                    return;
                }

                var delta = event.clientX - startX;
                rail.scrollLeft = startScrollLeft - delta;
            };

            var onPointerUp = function (event) {
                if (!isPointerDown) {
                    return;
                }

                isPointerDown = false;
                rail.classList.remove("is-dragging");

                if (typeof rail.hasPointerCapture === "function" && rail.hasPointerCapture(event.pointerId)) {
                    rail.releasePointerCapture(event.pointerId);
                }
            };

            var onMotionChange = function (event) {
                var nextSpeed = event.matches ? 22 : 66;
                if (nextSpeed !== speedPxPerSecond) {
                    speedPxPerSecond = nextSpeed;
                    lastTs = 0;
                }

                startRail();
            };

            rail.addEventListener("pointerdown", onPointerDown);
            rail.addEventListener("pointermove", onPointerMove);
            rail.addEventListener("pointerup", onPointerUp);
            rail.addEventListener("pointercancel", onPointerUp);
            rail.addEventListener("pointerleave", onPointerUp);
            rail.addEventListener("mouseenter", stopRail);
            rail.addEventListener("mouseleave", startRail);
            rail.addEventListener("focusin", stopRail);
            rail.addEventListener("focusout", startRail);

            if (typeof reducedMotion.addEventListener === "function") {
                reducedMotion.addEventListener("change", onMotionChange);
            } else if (typeof reducedMotion.addListener === "function") {
                reducedMotion.addListener(onMotionChange);
            }

            startRail();
        });
    }

    var galleryModal = document.querySelector("[data-gallery-modal]");
    if (galleryModal) {
        var galleryTitle = galleryModal.querySelector("[data-gallery-title]");
        var galleryText = galleryModal.querySelector("[data-gallery-text]");
        var galleryImage = galleryModal.querySelector("[data-gallery-image]");
        var galleryThumbs = galleryModal.querySelector("[data-gallery-thumbs]");
        var galleryPrev = galleryModal.querySelector("[data-gallery-prev]");
        var galleryNext = galleryModal.querySelector("[data-gallery-next]");
        var galleryClose = galleryModal.querySelector("[data-gallery-close]");
        var galleryItems = [];
        var galleryIndex = 0;

        var renderGallery = function () {
            if (!galleryItems.length || !galleryImage || !galleryThumbs) {
                return;
            }

            galleryImage.src = galleryItems[galleryIndex];
            galleryImage.alt = galleryTitle ? galleryTitle.textContent : "";
            galleryThumbs.innerHTML = "";

            galleryItems.forEach(function (item, index) {
                var thumbButton = document.createElement("button");
                var thumbImage = document.createElement("img");

                thumbButton.type = "button";
                thumbButton.className = "portfolio-gallery-thumb" + (index === galleryIndex ? " is-active" : "");
                thumbButton.setAttribute("aria-label", "View image " + (index + 1));

                thumbImage.src = item;
                thumbImage.alt = "";

                thumbButton.appendChild(thumbImage);
                thumbButton.addEventListener("click", function () {
                    galleryIndex = index;
                    renderGallery();
                });

                galleryThumbs.appendChild(thumbButton);
            });
        };

        var closeGallery = function () {
            galleryModal.hidden = true;
            document.body.classList.remove("gallery-open");
        };

        var openGallery = function (card) {
            var image = card.querySelector(".project-thumb");
            if (!image) {
                return;
            }

            var cardTitle = card.querySelector("h3");
            var cardText = card.querySelector("p");
            var sourceImages = card.getAttribute("data-gallery-images");

            galleryItems = sourceImages ? sourceImages.split("|") : [image.getAttribute("src")];
            galleryIndex = 0;

            if (galleryTitle) {
                galleryTitle.textContent = cardTitle ? cardTitle.textContent.trim() : "Project gallery";
            }

            if (galleryText) {
                galleryText.textContent = cardText ? cardText.textContent.trim() : "";
            }

            galleryModal.hidden = false;
            document.body.classList.add("gallery-open");
            renderGallery();
        };

        document.querySelectorAll(".page-work .project-card").forEach(function (card) {
            if (!card.querySelector(".project-thumb")) {
                return;
            }

            card.classList.add("is-clickable");
            card.tabIndex = 0;
            card.setAttribute("data-gallery-label", document.documentElement.lang === "en" ? "View gallery" : "Voir la galerie");

            card.addEventListener("click", function () {
                openGallery(card);
            });

            card.addEventListener("keydown", function (event) {
                if (event.key === "Enter" || event.key === " ") {
                    event.preventDefault();
                    openGallery(card);
                }
            });
        });

        if (galleryPrev) {
            galleryPrev.addEventListener("click", function () {
                galleryIndex = (galleryIndex - 1 + galleryItems.length) % galleryItems.length;
                renderGallery();
            });
        }

        if (galleryNext) {
            galleryNext.addEventListener("click", function () {
                galleryIndex = (galleryIndex + 1) % galleryItems.length;
                renderGallery();
            });
        }

        if (galleryClose) {
            galleryClose.addEventListener("click", closeGallery);
        }

        galleryModal.addEventListener("click", function (event) {
            if (event.target === galleryModal) {
                closeGallery();
            }
        });

        document.addEventListener("keydown", function (event) {
            if (!galleryModal.hidden && event.key === "Escape") {
                closeGallery();
            }
        });
    }

    if (contactForm) {
        var syncSummary = function () {
            var fields = {
                client: contactForm.querySelector("[name='client_type']"),
                project: contactForm.querySelector("[name='project_type']"),
                location: contactForm.querySelector("[name='location']"),
                timeline: contactForm.querySelector("[name='timeline']"),
            };

            Object.keys(fields).forEach(function (key) {
                var source = fields[key];
                var target = document.querySelector("[data-summary='" + key + "']");
                if (!source || !target) {
                    return;
                }

                var emptyLabel = target.getAttribute("data-empty") || (document.documentElement.lang === "en" ? "To be confirmed" : "À préciser");

                var value = source.value.trim();
                if (source.tagName === "SELECT") {
                    value = source.options[source.selectedIndex].text;
                }

                target.textContent = value || emptyLabel;
            });
        };

        contactForm.addEventListener("input", syncSummary);
        contactForm.addEventListener("change", syncSummary);
        syncSummary();

        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();

            var submitBtn = contactForm.querySelector('button[type="submit"]');
            var success = document.querySelector(".form-success");
            var errorEl = document.querySelector(".form-error");
            var btnText = submitBtn ? submitBtn.textContent : "";

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = "Envoi en cours…";
            }
            if (errorEl) errorEl.hidden = true;
            if (success) success.hidden = true;

            var formData = new FormData(contactForm);
            formData.append("_captcha", "false");
            formData.append("_template", "table");
            formData.append("_subject", "Nouvelle demande projet — " + (formData.get("full_name") || "Visiteur"));

            fetch("https://formsubmit.co/ajax/Contact@nexusdksgroup.com", {
                method: "POST",
                headers: { "Accept": "application/json" },
                body: formData
            })
            .then(function (res) { return res.json(); })
            .then(function (data) {
                if (data.success === "true" || data.success === true) {
                    if (success) success.hidden = false;
                    contactForm.reset();
                    syncSummary();
                } else {
                    if (errorEl) {
                        errorEl.textContent = data.message || "Une erreur est survenue.";
                        errorEl.hidden = false;
                    }
                }
            })
            .catch(function () {
                if (errorEl) {
                    errorEl.textContent = "Erreur réseau. Veuillez réessayer.";
                    errorEl.hidden = false;
                }
            })
            .finally(function () {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.textContent = btnText;
                }
            });
        });
    }

    /* ── Scroll to top ── */
    var scrollBtn = document.querySelector(".scroll-top-btn");
    if (scrollBtn) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 400) {
                scrollBtn.classList.add("is-visible");
            } else {
                scrollBtn.classList.remove("is-visible");
            }
        });
        scrollBtn.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    // ---- Pages services : outils-métier + configurateur → WhatsApp ----
    // Sélecteur « reco / diagnostic » : affiche le résultat lié à l'option choisie.
    document.querySelectorAll(".nx-reco-select").forEach(function (sel) {
        var scope = sel.closest(".svc-tool") || sel.closest("form");
        var out = scope ? scope.querySelector(".nx-reco-out") : null;
        sel.addEventListener("change", function () {
            if (!out) { return; }
            var opt = sel.options[sel.selectedIndex];
            var txt = opt ? opt.getAttribute("data-out") : "";
            if (txt) { out.textContent = txt; out.hidden = false; }
            else { out.hidden = true; }
        });
    });

    // Checklist de réception : barre de progression.
    document.querySelectorAll("[data-checklist]").forEach(function (tool) {
        var checks = tool.querySelectorAll("[data-check]");
        var bar = tool.querySelector(".nx-config-progress-bar");
        var label = tool.querySelector(".nx-config-progress-label");
        var total = checks.length;
        var update = function () {
            var n = tool.querySelectorAll("[data-check]:checked").length;
            if (bar) { bar.style.setProperty("--p", Math.round((n / total) * 100) + "%"); }
            if (label) { label.textContent = n + " / " + total; }
        };
        checks.forEach(function (c) { c.addEventListener("change", update); });
    });

    // Bouton « Préparer ma demande WhatsApp » : assemble un message structuré.
    document.querySelectorAll("[data-wa-build]").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var form = btn.closest(".nx-config");
            if (!form) { return; }
            var scope = form.closest(".svc-config-wrap") || form;
            var wa = form.getAttribute("data-wa");
            var service = form.getAttribute("data-service");
            var lines = ["Bonjour NEXUS DKS GROUP,", "Je souhaite un devis pour : " + service + ".", ""];
            scope.querySelectorAll("[data-field]").forEach(function (f) {
                var val = (f.value || "").trim();
                if (val) { lines.push("• " + f.getAttribute("data-label") + " : " + val); }
            });
            var groups = {};
            scope.querySelectorAll("[data-check]:checked").forEach(function (c) {
                var g = c.getAttribute("data-group") || "Éléments";
                (groups[g] = groups[g] || []).push(c.value);
            });
            Object.keys(groups).forEach(function (g) {
                lines.push("• " + g + " : " + groups[g].join(", "));
            });
            lines.push("", "Merci de me faire une proposition en FCFA.");
            window.open("https://wa.me/" + wa + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
        });
    });
});
