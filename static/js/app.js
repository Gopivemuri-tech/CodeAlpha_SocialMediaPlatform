(() => {
  const modal = document.getElementById('createModal');
  const openers = document.querySelectorAll('[data-open-create]');
  const closers = document.querySelectorAll('[data-close-create]');
  const open = () => { if (!modal) return; modal.classList.add('open'); modal.setAttribute('aria-hidden','false'); document.body.classList.add('modal-open'); setTimeout(() => modal.querySelector('textarea')?.focus(), 50); };
  const close = () => { if (!modal) return; modal.classList.remove('open'); modal.setAttribute('aria-hidden','true'); document.body.classList.remove('modal-open'); };
  openers.forEach(el => el.addEventListener('click', open));
  closers.forEach(el => el.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  document.querySelectorAll('[data-focus-comment]').forEach(btn => btn.addEventListener('click', () => document.getElementById(btn.dataset.focusComment)?.focus()));
})();
