'use strict';

const dialog = document.querySelector('#share-dialog');
const copyInput = document.querySelector('#post-link');
const feedback = document.querySelector('#feedback');
let sharePost;

function shareLinks(post) {
  const url = encodeURIComponent(post.url);
  return {li:'https://www.linkedin.com/sharing/share-offsite/?url='+url, fb:'https://www.facebook.com/sharer/sharer.php?u='+url, x:'https://x.com/intent/tweet?url='+url+'&text='+encodeURIComponent(post.title)};
}
function openShare(post) {
  sharePost=post;
  const links=shareLinks(post);
  copyInput.value=post.url;
  for (const [key, link] of Object.entries(links)) document.querySelector('#share-'+key).href=link;
  document.querySelector('#device-share').hidden=typeof navigator.share!=='function';
  feedback.textContent='';
  dialog.showModal();
}
document.querySelector('#copy-link').addEventListener('click',async () => {
  try {await navigator.clipboard.writeText(sharePost.url);feedback.textContent='Post link copied.';}
  catch {copyInput.focus();copyInput.select();feedback.textContent='Link selected. Press Ctrl+C or Command+C to copy.';}
});
document.querySelector('#device-share').addEventListener('click',async () => {
  try {await navigator.share({title:sharePost.title,url:sharePost.url});}
  catch (error) {if(error.name!=='AbortError') feedback.textContent='Use Copy link or choose a platform above.';}
});
document.querySelector('#download-card').addEventListener('click',async () => {
  const post=sharePost;
  const canvas=document.createElement('canvas');canvas.width=1080;canvas.height=1350;
  const ctx=canvas.getContext('2d');
  const img=new Image();img.src=post.image;
  try {await img.decode();} catch {feedback.textContent='The cover image could not be loaded.';return;}
  ctx.fillStyle='#15121f';ctx.fillRect(0,0,1080,1350);
  ctx.fillStyle='#cbb8ff';ctx.font='bold 33px system-ui';ctx.fillText('NOTES FROM THE WORK',68,99);
  ctx.fillStyle='#262034';ctx.fillRect(68,154,944,532);
  const scale=Math.min(944/img.width,532/img.height);
  ctx.drawImage(img,540-img.width*scale/2,420-img.height*scale/2,img.width*scale,img.height*scale);
  ctx.font='bold 62px system-ui';ctx.fillStyle='#f6f3ff';
  const lines=[];let line='';
  for(const word of post.title.split(' ')){
    const joined=line ? line+' '+word : word;
    if(line && ctx.measureText(joined).width>944){lines.push(line);line=word;}else{line=joined;}
  }
  if(line) lines.push(line);
  lines.forEach((part,i)=>ctx.fillText(part,68,790+i*76));
  ctx.fillStyle='#cbb8ff';ctx.font='bold 34px system-ui';ctx.fillText('Keith Ornbaum',68,1200);
  ctx.fillStyle='#d0c9de';ctx.font='30px system-ui';ctx.fillText('ornbaumkeith.github.io/blog',68,1250);
  const anchor=document.createElement('a');anchor.download=post.id+'-instagram.png';anchor.href=canvas.toDataURL('image/png');anchor.click();
  feedback.textContent='Instagram graphic downloaded.';
});

document.querySelectorAll('[data-share]').forEach(button => {
  if (typeof dialog.showModal !== 'function') return;
  button.hidden = false;
  button.addEventListener('click', () => {
    const {shareTitle:title, shareUrl:url, shareImage:image, shareSlug:id} = button.dataset;
    openShare({title,url,image,id});
  });
});
document.querySelectorAll('.toc a').forEach(link => {
  link.addEventListener('click', () => {
    const heading = document.getElementById(link.hash.slice(1));
    heading?.focus({preventScroll:true});
  });
});

const controls = document.querySelector('.blog-controls');
if (controls) {
  const cards = document.querySelector('#cards');
  const posts = Array.from(cards.children).sort((a,b) => b.dataset.date.localeCompare(a.dataset.date));
  const search = document.querySelector('#search');
  const sort = document.querySelector('#sort');
  const result = document.querySelector('#results');
  const empty = document.querySelector('#empty');
  const buttons = Array.from(document.querySelectorAll('[data-filter]'));
  const all = buttons[0].dataset.filter;
  let selected = all;

  function updateArchive() {
    const query = search.value.trim().toLowerCase();
    const defaultView = !query && selected === all && sort.value === 'newest';
    const ordered = sort.value === 'oldest' ? posts.slice().reverse() : posts;
    let visible = 0;
    ordered.forEach(post => {
      const category = post.dataset.archivePost.split(' | ');
      const matchesTopic = selected === all || category.includes(selected);
      const matchesQuery = [post.textContent, ...category].join(' ').toLowerCase().includes(query);
      post.hidden = !matchesTopic || !matchesQuery || (defaultView && post.hasAttribute('data-featured'));
      if (!post.hidden) visible++;
    });
    cards.append(...ordered);
    result.textContent = visible + (visible === 1 ? ' post' : ' posts') + (defaultView ? ' in the archive' : '');
    empty.hidden = visible > 0;
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === selected)));
  }
  buttons.forEach(button => button.addEventListener('click', () => {
    selected = button.dataset.filter;
    updateArchive();
  }));
  document.querySelector('#reset').addEventListener('click', () => {
    search.value = '';
    sort.value = 'newest';
    selected = all;
    updateArchive();
    search.focus();
  });
  search.addEventListener('input', updateArchive);
  sort.addEventListener('change', updateArchive);
  updateArchive();
  controls.hidden = false;
  result.hidden = false;
}
