# Caza — infoproductos con VSL en Brasil: salud y renta extra (2026-11-02, 2ª pasada)

Corrección de la 1ª pasada: lo que entregué antes (LIQUIDZ, DRM Plus, Dra. Caroline Townsend) eran **productos físicos**, y Venda Sem Estoque es **marca personal**. Nada de eso era infoproducto. Esta pasada busca únicamente **infoproducto digital con VSL**.

Método: ~40 búsquedas en `ads_library_search` + ~2.000 anuncios escaneados en la Biblioteca de Anuncios (UI) + verificación de landings en Chrome.

## El hallazgo que manda sobre todo lo demás

**El embudo de VSL está prácticamente extinto en Meta Brasil.**

Prueba dura: barrido del universo de video activo en Brasil (query `você`, `media_type=video`, 321 anuncios muestreados). Anunciantes con creativo de **más de 110 segundos: 4**. Ninguno con volumen. Repetido con `"renda extra"` (270 anuncios): el de más volumen con video >90s es una empresa de fletes.

El mercado brasileño migró a **creativo corto (8–60s) → WhatsApp, Instagram o checkout directo**. La VSL larga ya no es donde está el dinero ahí.

## Cómo está estructurado el infoproducto brasileño (lo que explica por qué no hay 50+)

| Tipo | Volumen por fanpage | VSL | Infoproducto | No personal |
|---|---|---|---|---|
| Infoproducto low ticket de afiliado | **1–48** | ✗ (ads de 8–30s) | ✓ | ✓ |
| Lanzamiento perpetuo con VSL | 50–140 | ✓ | ✓ | ✗ (marca personal) |
| Nutra física → WhatsApp | 50–130 | ✗ | ✗ | ✓ |
| E-commerce / revenda | 100–670 | ✗ | ✗ | ✓ |

El low ticket brasileño **rota decenas de fanpages con pocos ads cada una** (cuentas sucias de afiliado). Por eso el filtro de "+50 ads en una fanpage" excluye por construcción a casi todo el infoproducto. Verificado en: Receitas para Diabéticos (6), Pack De Achadinhos Shopee (1), Juliana Figurinhas (0), Essência da Beleza Diária (1), Homens com Propósito (5), Receitas da Vó Benita (3), Fundação UniHealth (22), Michaelle Almeida Nails (9), Insta Criativo (16), Olhos que Encantam (16).

## Lo mejor que existe hoy con el perfil que pediste

### 1. Arquivos que encantam — el más cerca del perfil completo
- `facebook.com/ads/library/?view_all_page_id=216603914872916`
- **48 anuncios activos** en BR · corriendo desde el **15/10** (18 días)
- **Infoproducto digital puro:** Kit Lembrancinhas — +150 revistinhas para colorir + 800 convites editáveis no Canva
- **R$10** · página **no personal** ✓ · nicho **renta extra** (vender lembrancinhas para festas infantis) ✓
- **Duplicación brutal:** el creativo `🚨Apenas R$10 🚨` repetido ~45 veces
- ✗ **No es VSL:** los ads son de **0:08**, el display link (`kitrevistinhasdecolorir.com`) es falso (NXDOMAIN) y el embudo es ad corto → página de ventas con checkout
- Cluster: la frase "Atividades que Encantam" tiene **194 anuncios activos** sumando players → nicho validado con varios competidores

### 2. Venda Sem Estoque — la única con VSL verificada y 50+
- page_id `598638986661794` · **~110 anuncios activos**
- **VSL real:** `site.marcelowedrop.com`, headline `📣 A aula está liberada`, videos de **1:41 a 3:51**, sin pausar desde el 24/09
- Infoproducto (aula/mentoria de vender sin stock) ✓ · nicho renta extra ✓
- ✗ Marca personal: Marcelo Menezes (`@marcelomenezesfc`), el dominio lleva su nombre

### 3. Suellen Souza — infoproducto low ticket con volumen
- page_id `103284572789476` · **110 anuncios activos** · 3+ días
- **De R$197 por R$35** · `⭐⭐⭐⭐⭐(4.9/5)`
- ✗ Nicho ventas/closing (no salud ni renta extra) · ✗ embudo a Instagram, no VSL

### 4. Notícia Saudável — el mejor advertorial de salud
- page_id `106345615557584` · **32 anuncios activos** · ~5 días
- Página advertorial no personal ✓ · nicho **salud** (sueño) ✓
- Ángulos: `Dormir Bem Nunca Foi Tão Fácil` · `Aprovado por Médicos`
- ✗ No llega a 50

## Veredicto

Los cuatro criterios juntos — **infoproducto + VSL + 50 ads + no marca personal + salud/renta extra + Brasil** — **no se cumplen en ninguna oferta hoy**. No es que no busqué: la celda está vacía porque el mercado brasileño abandonó la VSL.

Hay que mover un criterio. Las tres salidas, por orden de lo que yo haría:

1. **Cambiar de mercado, mantener la VSL.** La VSL sigue siendo el embudo dominante en EE.UU. Si el requisito no negociable es VSL, hay que cazar en inglés, no en portugués.
2. **Mantener Brasil, cambiar de embudo.** Lo que convierte ahí hoy es creativo corto → página de ventas con checkout (Arquivos que encantam, 48 ads, R$10) o creativo corto → WhatsApp. El modelo a copiar es ese, no la VSL.
3. **Mantener todo, bajar el volumen a 20–48 ads.** A ese nivel sí hay infoproducto de salud y renta extra con página no personal: Arquivos que encantam (48), Notícia Saudável (32), Fundação UniHealth (22).

## Footprints de búsqueda (para no repetir el trabajo)

**Sirven para aislar infoproducto:** `kiwify`, `hotmart` en el texto del creativo (15.800 y varios miles de ads, puro infoproducto); precio en el link title (`Apenas R$10`, `por R$ 17,90`, `De R$197 por R$35`).

**Sirven para aislar VSL:** `media_type=video` + filtrar por duración del creativo >90s en el UI; `VER COMPLETO`, `a aula está liberada`, `antes de sair do ar`.

**Solo traen ruido en Brasil:** `renda extra`, `emagrecer`, `antes de dormir`, `por apenas R$`, `aula gratuita`, `assista ao vídeo` — los invade el comercio local, las apps de microdrama y los coaches de marca personal.

**Trampa a evitar:** el dominio que muestra la Biblioteca de Anuncios es el *display link* y suele ser **falso** (no resuelve en DNS). No se puede verificar una landing por ahí.
