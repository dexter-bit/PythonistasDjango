jQuery(document).ready(function () {
    // This button will increment the value
    $('.qtyplus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('field');
        // Get its current value
        var currentVal = parseInt($('input[name=' + fieldName + ']').val());
        // If is not undefined
        if (!isNaN(currentVal)) {
            // Increment
            $('input[name=' + fieldName + ']').val(currentVal + 1);
        } else {
            // Otherwise put a 0 there
            $('input[name=' + fieldName + ']').val(0);
        }
    });
    // This button will decrement the value till 0
    $(".qtyminus").click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('field');
        // Get its current value
        var currentVal = parseInt($('input[name=' + fieldName + ']').val());
        // If it isn't undefined or its greater than 0
        if (!isNaN(currentVal) && currentVal > 0) {
            // Decrement one
            $('input[name=' + fieldName + ']').val(currentVal - 1);
        } else {
            // Otherwise put a 0 there
            $('input[name=' + fieldName + ']').val(0);
        }
    });

    $("#target").submit(function (event) {
        alert("Handler for .submit() called.");
        event.preventDefault();
    });

});

(function () {
    var propParallax = {

        seccion: document.querySelector('.parallax'),
        recorrido: 0,
        limite: 0,

    }


    var metParallax = {

        Start: function () {

            window.addEventListener('scroll', metParallax.scrollParallax);

        },

        scrollParallax: function () {

            propParallax.recorrido = window.pageYOffset;
            propParallax.limite = propParallax.seccion.offsetTop + propParallax.seccion.offsetHeight;

            if (propParallax.recorrido > propParallax.seccion.offsetTop - window.outerHeight && propParallax.recorrido <= propParallax.limite) {

                propParallax.seccion.style.backgroundPositionY = (propParallax.recorrido - propParallax.seccion.offsetTop) / 2.5 + 'px';

            } else {
                propParallax.seccion.style.backgroundPositionY = 1;
            }
        }

    }

    metParallax.Start();
}());


var propScroll = {

    posicion: window.pageYOffset,
    scroll_suave: document.getElementsByClassName('scroll-suave'),
    volver_suave: document.getElementsByClassName('volver-suave'),
    destino: null,
    seccion_distancia: null,
    intervalo: null
    
    
    }
    
    
    var metScroll = {
    
        Start: function(){
    
            for (var i = 0; i < propScroll.scroll_suave.length; i++) {
                propScroll.scroll_suave[i].addEventListener('click', metScroll.moverse);
            }
    
            for (var i = 0; i < propScroll.volver_suave.length; i++) {
                propScroll.volver_suave[i].addEventListener('click', metScroll.volver);
            }
    
    
    
            
        },
    
    
        moverse: function (e) {
            e.preventDefault();
    
            clearInterval(propScroll.intervalo);
            propScroll.destino = this.getAttribute('href');
            propScroll.seccion_distancia = document.querySelector(propScroll.destino).offsetTop - 94;
    
            propScroll.posicion = window.pageYOffset;
            propScroll.intervalo = setInterval(function() {
    
    
                if (propScroll.posicion < propScroll.seccion_distancia) {
    
    
                    propScroll.posicion += 30;
    
                    if (propScroll.posicion >= propScroll.seccion_distancia) {
    
                        clearInterval(propScroll.intervalo);
                    }
    
                } else {
    
                    propScroll.posicion -= 30;
    
                    if (propScroll.posicion <= propScroll.seccion_distancia) {
    
                        clearInterval(propScroll.intervalo);
                    }
    
                }
    
    
                    window.scrollTo(0, propScroll.posicion);
    
    
            }, 15);
        },
    
    
        volver: function (e) {
            e.preventDefault();
    
            clearInterval(propScroll.intervalo);
            propScroll.posicion = window.pageYOffset;
            propScroll.intervalo = setInterval(function() {
    
                if (propScroll.posicion > 0) {
    
                    propScroll.posicion -=30;
    
                    if (propScroll.posicion <= 0) {
    
                        clearInterval(propScroll.intervalo);
                    }
    
                } else {
    
                    return;
                }
    
                window.scrollTo(0, propScroll.posicion);
    
            }, 15);
    
        }
    
    }
    
    metScroll.Start();