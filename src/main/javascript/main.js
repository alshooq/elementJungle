const ELEMENTS = ['nickel', 'palladium', 'platinum', 'darmstadtium'];

// Pega índice do elemento pelo nome
function getElementIndex(name) {
  return ELEMENTS.indexOf(name.toLowerCase());
}

// Pega o elemento atual baseado na URL (/nickel/ etc)
function getCurrentElement() {
  const path = window.location.pathname.toLowerCase();
  for (const el of ELEMENTS) {
    if (path.includes(`/${el}/`)) return el;
  }
  return ELEMENTS[0]; // default nickel
}

// Fetch JSON do backend
async function fetchElementData(elementIndex, page) {
  const res = await fetch('/data/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ element: elementIndex, page }),
  });
  return await res.json();
}

// Cria a sidebar lateral fixa, oculta no mobile (<768px)
function createSidebar(currentElement) {
  const aside = document.createElement('aside');
  aside.className = `
    fixed left-0 top-0 h-full w-20 md:w-28 bg-black bg-opacity-80
    flex flex-col items-center py-8 gap-6 shadow-xl border-r border-pink-600
    z-50
    hidden md:flex
  `;

  ELEMENTS.forEach((element, index) => {
    const img = document.createElement('img');
    img.src = `/img/elements/${index}.png`;
    img.alt = element;
    img.title = element.charAt(0).toUpperCase() + element.slice(1);
    img.className = `
      w-14 h-14 object-contain cursor-pointer rounded transition-transform duration-300
      hover:scale-110
      ${element === currentElement ? 'ring-4 ring-pink-500' : ''}
    `;

    img.onclick = () => {
      if (element !== currentElement) {
        window.location.href = `/${element}/`;
      }
    };

    aside.appendChild(img);
  });

  return aside;
}

// Alterar renderContent para receber o parâmetro 'page'
function renderContent(container, data, currentElement, page) {
  container.innerHTML = '';

  // Título com ícone
  const title = document.createElement('h2');
  title.className = 'text-4xl font-extrabold mb-8 text-pink-400 drop-shadow-md flex items-center gap-4 justify-center flex-wrap';

  const icon = document.createElement('img');
  const index = getElementIndex(currentElement);
  icon.src = `/img/elements/${index}.png`;
  icon.alt = currentElement;
  icon.className = 'w-14 h-14 object-contain';

  title.appendChild(icon);
  title.appendChild(document.createTextNode(data.Nome));
  container.appendChild(title);

  const contentBlock = document.createElement('div');
  contentBlock.className = 'max-w-3xl mx-auto bg-gray-900 bg-opacity-90 rounded-xl p-8 shadow-lg';


  // **Se for página 2, insere a imagem GIF do átomo**
  if (page === 2) {
    const gif = document.createElement('video');
    gif.src = `/img/atoms/${index}/${index}.mp4`;
    gif.autoplay = true;
    gif.loop = true;
    gif.muted = true;
    gif.playsInline = true;
    gif.className = 'mx-auto mb-8 w-48 h-auto rounded-md shadow-lg';
    contentBlock.appendChild(gif);
    
  }

  // Itera sobre campos, ignora nome
  Object.entries(data).forEach(([key, value]) => {
    if (key === 'Nome') return;

    const fieldContainer = document.createElement('div');
    fieldContainer.className = 'mb-7';

    // Subtítulo com efeito hover
    const subtitle = document.createElement('h3');
    subtitle.className = `
      text-xl font-semibold mb-2 cursor-pointer
      transition-transform duration-300 ease-in-out
      hover:text-pink-400 hover:-translate-y-1
      flex items-center gap-2 select-none
    `;

    // Ícone pequeno ao lado do subtítulo
    const smallIcon = document.createElement('img');
    smallIcon.src = `/img/elements/${index}.png`;
    smallIcon.alt = key;
    smallIcon.className = 'w-5 h-5 object-contain';

    subtitle.appendChild(smallIcon);
    subtitle.appendChild(document.createTextNode(key.replace(/_/g, ' ')));
    fieldContainer.appendChild(subtitle);

    const paragraph = document.createElement('p');
    paragraph.className = 'text-gray-300 leading-relaxed';
    paragraph.textContent = value;
    fieldContainer.appendChild(paragraph);

    contentBlock.appendChild(fieldContainer);
  });

  container.appendChild(contentBlock);

}

// Renderiza nav das páginas com botões pulantes
function createPagination(elementIndex, container, onPageChange) {
  const pageTitles = ['Informações Gerais', 'Distribuição Eletrônica', 'Informações Específicas'];
  let currentPage = 1;

  const nav = document.createElement('nav');
  nav.className = 'mb-10 flex flex-wrap justify-center gap-4';

  pageTitles.forEach((title, i) => {
    const btn = document.createElement('button');
    btn.textContent = title;
    btn.className = `
      px-5 py-2 rounded-lg bg-pink-700 hover:bg-pink-600 text-white
      transition transform duration-300 ease-in-out
      hover:-translate-y-1 hover:scale-105 shadow-lg
      text-sm md:text-base font-semibold
      focus:outline-none focus:ring-2 focus:ring-pink-400
      ${i+1 === currentPage ? 'ring-2 ring-pink-400' : ''}
    `;

    btn.onclick = () => {
      if (currentPage !== i + 1) {
        currentPage = i + 1;
        // Atualiza classe active nos botões
        [...nav.children].forEach((b, idx) => {
          b.classList.toggle('ring-2', idx === i);
          b.classList.toggle('ring-pink-400', idx === i);
        });
        onPageChange(currentPage);
      }
    };

    nav.appendChild(btn);
  });

  container.appendChild(nav);

  // Função para atualizar conteúdo da página
  return (page) => {
    currentPage = page;
    onPageChange(page);
    // Atualiza botão ativo
    [...nav.children].forEach((b, idx) => {
      b.classList.toggle('ring-2', idx === page-1);
      b.classList.toggle('ring-pink-400', idx === page-1);
    });
  };
}

function initJungleApp() {
  const currentElement = getCurrentElement();
  const main = document.getElementById('jungle-root');

  if (!main) return;

  // Cria vídeo de fundo só uma vez (se não existir)
  if (!document.getElementById('bg-video')) {
    const video = document.createElement('video');
    video.id = 'bg-video';
    video.src = '/img/local/init/atoms.mp4';
    video.playbackRate = 0.8;
    video.autoplay = true;
    video.loop = true;
    video.muted = true;
    video.playsInline = true;
    document.body.appendChild(video);
  }

  // Remove sidebar antiga se existir
  const oldSidebar = document.querySelector('aside');
  if (oldSidebar) oldSidebar.remove();

  // Cria sidebar (apenas para md+)
  const sidebar = createSidebar(currentElement);
  document.body.appendChild(sidebar);

  // Limpa main e deixa opacity 0 (invisível)
  main.innerHTML = '';
  main.classList.remove('visible');

  // Cria container para paginação + conteúdo
  const container = document.createElement('div');
  container.className = 'w-full';
  main.appendChild(container);

  // Cria navegação da paginação
  const changePage = (page) => {
    // Enquanto carrega, opcional: desativa interações
    main.style.pointerEvents = 'none';

    fetchElementData(getElementIndex(currentElement), page)
      .then(data => {
        renderContent(container, data, currentElement, page);
        // Fade in suave quando conteúdo estiver pronto
        main.classList.add('visible');
        main.style.pointerEvents = 'auto';
      })
      .catch(() => {
        container.innerHTML = '<p class="text-center text-red-500">Erro ao carregar os dados.</p>';
        main.classList.add('visible');
        main.style.pointerEvents = 'auto';
      });
  };

  const updatePagination = createPagination(getElementIndex(currentElement), main, changePage);

  // Carrega a página 1 inicialmente
  updatePagination(1);
}

document.addEventListener('DOMContentLoaded', initJungleApp);