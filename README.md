
# Proyecto $\Lambda CDM$

En la presente notebook, en forma de resumen, se muestran resultados teóricos, así como el código que se utiliza para hacer estimaciones, de tal forma de corroborar la teoría.

## Ley de Hubble

Hubble y Humason, hicieron observaciones, las cuales les ayudaron a estimar dos importantes resultados

1. Distancia de decenas de galaxias.
2. Uno de los resultados que se utilizaran más adelante, es la proyección de su velocidad a lo largo de la línea de visión conocida como "_**velocidad de recesión**_", la cual se mide partiendo del corrimiento Doppler de la luz emitida por estrellas, algo importante a destacar es que se percataron de que entre más lejana es una galaxia, mayor es la velocidad de recesión. Además, la distancio y velocidad de recesión son proporcionales, y más aún la constante de proporcionalidad es la misma para todas las galaxias, de esta manera llegaron a lo que se conoce como **"Ley de Hubble"**

<p style="border:2px solid Tomato;"> $$V_r = H_0 d_L$$ </p>

Donde 

- $H_0 \simeq 70 km/s Mpc^{-1} \rightarrow$  corresponde a la constante de Hubble
- $d_L \rightarrow$ distancia luminosa


## Coordenadas comoviles, coordenadas propias y factor de escala

<p style="color:rgb(71, 178, 255);"> "Coordenadas comoviles"</p>

- Etiqueta de la posición de las partículas, donde dichas partículas son galaxias, también se conoce como coordenadas de un <p style="color:Orange;">"observador comovil"</p>

<p style="color:rgb(71, 178, 255);"> "Observador comovil"</p>

- En un espacio curvo, es aquel que viaja anclado a partículas de prueba, la cual está aislada de otras partículas, la cual se mueve a lo largo de geodésicas de la métrica del espacio curvo, en las geodésicas de un universo homogéneo e isótropo, en expansión, sus coordenadas están “ancladas” a la expansión.

Algo importante a mencionar, es que cuando hablamos de coordenadas comoviles las etiquetas no cambian, sin embargo, en el caso de las coordenadas físicas las etiquetas de los puntos sí cambian, a estas también se les conoce como <span style="color:Orange;">coordenadas propias</span> y están dadas por

<p style="border:2px solid Tomato;"> $$\begin{equation} r=a(t)x \end{equation}$$ </p>

Donde

$a(t)\rightarrow$  es el <span style="color: Orange;"> factor de escala</span>, que es una tasa de crecimiento de las distancias.

Partiendo de la anterior ecuación, se puede deducir la ley de Hubble, únicamente se hace la derivada respecto al tiempo.

$$\begin{equation} v_r=\dot{r}=\frac{\dot{a}}{a}ax+a\dot{x} \end{equation}$$ 

donde $r$ corresponde a la posición de una galaxia aislada, además se puede ignorar el segundo término del lado derecho, y adicional a esto se puede definir la tasa como $H$ es decir $H(t)=\frac{\dot{a}}{a}$, lo cual queda como 

<p style="border:2px solid Tomato;"> $$\begin{equation} v_r=H(t)r \end{equation}$$ </p>

Que corresponde a la velocidad de recesión


## Métrica de Friedmann-Robertson-Walker (FRW)

La métrica de LFRW representa la geometría que mejor se adapta al principio cosmológico y las observaciones de la expansión del universo, además esta se puede asociar a un elemento diferencial de línea que proporciona una forma de calcular distancias infinitesimales en dicho espacio, dicho lo anterior, esta métrica se representa de la siguiente manera.

<p style="border:2px solid Tomato;"> $$\begin{equation} ds^2 = dt^2 - a^2(t)\left[\frac{dr^2}{1-kr^2}+r^2d\theta^2+r^2\sin^2{\theta}d\phi^2\right]\end{equation}$$ </p>

En este caso, como ya mencionamos, el factor de escala se representa como $a(t)$, y, por otra parte, la coordenada radial $r$ no tiene unidades, y además $k$ representa el tipo de curvatura del espacio, y puede adquirir los siguientes valores.

<p style="color:Orange;"> $$k= \begin{cases}+1 & \text { universo cerrado } \\ 0 & \text { universo plano } \\ -1 & \text { universo abierto }\end{cases}$$ </p>

Estos valores son independientes del tamaño del universo, además si nuestro universo es plano o abierto, puede ser infinitamente grande, sin embargo, para el caso $k=+1$, se puede mostrar que la métrica LFRW corresponde a la métrica de una esfera.

Por otra parte, si consideramos que el universo se rige por las ecuaciones de Einstein. 

<p style="border:2px solid Tomato;">$$R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R = 8\pi T_{\mu\nu}$$</p>

Donde $R_{\mu\nu}$ corresponde al tensro de Ricci, $R$ se le conoce como escalar de Ricci, $T_{\mu\nu}$ corresponde al tensor de energía-momento y, finalmente, $g_{\mu\nu}$ es la metrica.

Además, el tensor de energía-momento tiene la forma siguiente.

$$\left(T^\mu_{\nu}\right) = diag(\rho,-P,-P,-P)$$

Donde $\rho$ corresponde a la densidad de energía y $P$ la presión del fluido, de manera que el universo se puede modelar como un fluido perfecto.

Por otra parte las componentes no nulas del tensor de Ricci están dadas de la siguiente manera 

$$
R_{00} = -3 \frac{\ddot{a}}{a}
$$

$$
R_{ij} = -\left[\frac{\ddot{a}}{a} + 2\left(\frac{\dot{a}}{a}\right)^2 +2\frac{k}{a^2}\right]g_{ij}
$$

y el escalar de Ricci 

$$
R = -6 \left[\frac{\ddot{a}}{a} + \left(\frac{\dot{a}}{a}\right)^2+\frac{k}{a^2}\right]
$$

Si consideramos la componente $(\mu,\nu)=(0,0)$  de la ecuacion de Einstein, y sustituyendo lo anterior, que son las compnente no nulas del tensor de Ricci, nos queda lo siguiente.

$$
R_{00}-\frac{1}{2}g_{00}R = 8\pi T_{00}
$$

$$
-3\frac{\ddot{a}}{a} + \frac{6}{2}\left[\frac{\ddot{a}}{a} + \left(\frac{\dot{a}}{a}\right)^2+\frac{k}{a^2}\right]=8\pi\rho
$$

Simplificando lo anterior nos queda lo siguiente 

$$\begin{equation}
3\left[\left(\frac{\dot{a}}{a}\right)^2+\frac{k}{a^2}\right] = 8\pi \rho
\end{equation}$$

O bien escrito de otra manera.

<p style="border:2px solid Tomato;">$$\begin{equation}
    \left(\frac{\dot{a}}{a}\right)^2 + \frac{k}{a^2} = \frac{8}{3}\pi\rho
    \end{equation}$$</p>

Recordando lo que se discutió en la sección de <span style="color:Orange;">Ley de Hubble</span> y la de <span style="color:Orange;">Coordenadas comoviles, coordenadas propias y el factor de escala</span>, la anterior ecuación se puede reescribir de la siguiente forma.

<p style="border:2px solid Tomato;">$$\begin{equation}
    H^2 + \frac{k}{a^2} = \frac{8}{3}\pi\rho
    \end{equation}$$</p>

La cual se conoce como <span style="color:Orange;">La ecuación de Friedmann</span>
