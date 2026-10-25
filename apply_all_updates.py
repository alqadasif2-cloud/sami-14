with open('public/assets/index-DoqMLvwt.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Format Helper at top
helper = 'window.__formatSamiMemberCount=function(n){if(n===void 0||n===null||n===""||isNaN(n))return"";var num=Number(n);if(num>=1000000){var v=num/1000000;return(v%1===0?v.toString():v.toFixed(1).replace(/\\.0$/,""))+" مليون"}if(num>=1000){var v=num/1000;return(v%1===0?v.toString():v.toFixed(1).replace(/\\.0$/,""))+" ألف"}return num.toString()};'
if 'window.__formatSamiMemberCount' not in content:
    content = helper + content

# 2. Hide explanation text in supervisor modal (Requirement 2)
t_expl = '(0,$.jsx)(`div`,{className:`p-3 rounded-2xl bg-amber-500/10 border border-amber-500/25 text-xs text-amber-200 leading-relaxed`,children:`اختر المشرف الذي ترغب في محادثته. سيتم فتح المحادثة الخاصة وتجهيز رسالتك في مربع الكتابة لتراجعها وترسلها متى شئت.`})'
assert t_expl in content, "t_expl not found"
content = content.replace(t_expl, 'null')

# 3. Default supervisor avatar in contact modal (Requirement 1, point 1)
t_sup_def = '(0,$.jsx)(`div`,{className:`w-11 h-11 rounded-2xl bg-amber-400 text-slate-950 flex items-center justify-center font-bold text-lg shadow-md shrink-0`,children:y.id===1?`👑`:`🌟`})'
r_sup_def = 'y.avatarUrl?(0,$.jsx)(PC,{src:y.avatarUrl,alt:y.displayName,className:`w-11 h-11 rounded-2xl object-cover border-2 border-amber-400 shadow-md shrink-0`,fallbackIcon:(0,$.jsx)(`div`,{className:`w-11 h-11 rounded-2xl bg-amber-400 text-slate-950 flex items-center justify-center font-bold text-lg shadow-md shrink-0`,children:y.id===1?`👑`:`🌟`})}):(0,$.jsx)(`div`,{className:`w-11 h-11 rounded-2xl bg-amber-400 text-slate-950 flex items-center justify-center font-bold text-lg shadow-md shrink-0`,children:y.id===1?`👑`:`🌟`})'
assert t_sup_def in content, "t_sup_def not found"
content = content.replace(t_sup_def, r_sup_def)

# 4. Other supervisors list avatars in contact modal (Requirement 1, point 1 & 4)
t_sup_list = '(0,$.jsx)(`div`,{className:`w-10 h-10 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-amber-400 shrink-0`,children:e.id===1?`👑`:`🛡️`})'
r_sup_list = 'e.avatarUrl?(0,$.jsx)(PC,{src:e.avatarUrl,alt:e.displayName,className:`w-10 h-10 rounded-xl object-cover border border-slate-700 shrink-0`,fallbackIcon:(0,$.jsx)(`div`,{className:`w-10 h-10 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-amber-400 shrink-0`,children:e.id===1?`👑`:`🛡️`})}):(0,$.jsx)(`div`,{className:`w-10 h-10 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-amber-400 shrink-0`,children:e.id===1?`👑`:`🛡️`})'
assert t_sup_list in content, "t_sup_list not found"
content = content.replace(t_sup_list, r_sup_list)

# 5. Private chat header with supervisor avatar (Requirement 1, point 2)
t_chat_head = 'children:[(0,$.jsx)(tS,{className:`w-4 h-4`}),(0,$.jsx)(`span`,{children:`رجوع`})]}),(0,$.jsxs)(`div`,{children:[(0,$.jsx)(`h2`,{className:`text-sm font-black text-amber-400`,'
r_chat_head = 'children:[(0,$.jsx)(tS,{className:`w-4 h-4`}),(0,$.jsx)(`span`,{children:`رجوع`})]}),(0,$.jsxs)(`div`,{className:`flex items-center gap-2.5`,children:[r?.avatarUrl?(0,$.jsx)(PC,{src:r.avatarUrl,alt:r.displayName||`مشرف`,className:`w-9 h-9 rounded-full object-cover border-2 border-amber-400/60 shadow shrink-0`,fallbackIcon:(0,$.jsx)(`div`,{className:`w-9 h-9 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-sm`,children:r?.id===1?`👑`:`🛡️`})}):(0,$.jsx)(`div`,{className:`w-9 h-9 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-sm shrink-0`,children:r?.id===1?`👑`:`🛡️`}),(0,$.jsxs)(`div`,{children:[(0,$.jsx)(`h2`,{className:`text-sm font-black text-amber-400`,'
assert t_chat_head in content, "t_chat_head not found"
content = content.replace(t_chat_head, r_chat_head)

# 6. Channel member count displays (Requirement 3, point 2 & 6)
t_mc1 = 'e.memberIds.length,` عضو`'
r_mc1 = '(e.displayMemberCount!=null&&e.displayMemberCount!==""?window.__formatSamiMemberCount(e.displayMemberCount):e.memberIds.length),` عضو`'
assert t_mc1 in content, "t_mc1 not found"
content = content.replace(t_mc1, r_mc1)

t_mc2 = 'v?.memberIds.length||0,` عضواً • حذف تلقائي بعد 48 ساعة`'
r_mc2 = '(v?.displayMemberCount!=null&&v?.displayMemberCount!==""?window.__formatSamiMemberCount(v.displayMemberCount):v?.memberIds.length||0),` عضواً • حذف تلقائي بعد 48 ساعة`'
assert t_mc2 in content, "t_mc2 not found"
content = content.replace(t_mc2, r_mc2)

# 7. Map displayMemberCount in $C channels subscriber (Requirement 3, point 4)
t_chan_map = 'createdBy:Number(n.createdBy||1),createdAt:Number(n.createdAt||Date.now()),updatedAt:Number(n.updatedAt||Date.now())})'
r_chan_map = 'createdBy:Number(n.createdBy||1),createdAt:Number(n.createdAt||Date.now()),updatedAt:Number(n.updatedAt||Date.now()),displayMemberCount:n.displayMemberCount!=null?Number(n.displayMemberCount):null})'
assert t_chan_map in content, "t_chan_map not found"
content = content.replace(t_chan_map, r_chan_map)

# 8. tw channel update - include displayMemberCount (Requirement 3, point 4)
t_tw = 'if(t.visibility!==void 0&&(n.visibility=t.visibility===`hidden`?`hidden`:`visible`),'
r_tw = 'if(t.displayMemberCount!==void 0&&(n.displayMemberCount=t.displayMemberCount),t.visibility!==void 0&&(n.visibility=t.visibility===`hidden`?`hidden`:`visible`),'
assert t_tw in content, "t_tw not found"
content = content.replace(t_tw, r_tw)

# 9. ew channel create - include displayMemberCount
t_ew1 = 'createdAt:t,updatedAt:t};return await ov(K(Z,zC,n),{'
r_ew1 = 'createdAt:t,updatedAt:t,displayMemberCount:e.displayMemberCount!==void 0?e.displayMemberCount:null};return await ov(K(Z,zC,n),{'
assert t_ew1 in content, "t_ew1 not found"
content = content.replace(t_ew1, r_ew1)

t_ew2 = 'createdBy:1,createdAt:t,updatedAt:t}),c}'
r_ew2 = 'createdBy:1,createdAt:t,updatedAt:t,displayMemberCount:c.displayMemberCount}),c}'
assert t_ew2 in content, "t_ew2 not found"
content = content.replace(t_ew2, r_ew2)

# 10. Channel edit & create modal hooks and submit handler (Requirement 3, point 1, 5, 8)
t_je = 'Je=e=>{ye(e),xe(e.name),Ce(e.password),E(e.visibility||`visible`),Te(e.memberIds),De(null),ke(e.imageUrl||null),Ae(!1),ve(!0)}'
r_je = 'Je=e=>{ye(e),xe(e.name),Ce(e.password),E(e.visibility||`visible`),Te(e.memberIds),De(null),ke(e.imageUrl||null),Ae(!1),ve(!0),setTimeout(()=>{let el=document.getElementById("sami_dmc_input");if(el)el.value=(e.displayMemberCount!=null?e.displayMemberCount:"")},40)}'
assert t_je in content, "t_je not found"
content = content.replace(t_je, r_je)

t_qe = 'qe=()=>{ye(null),xe(``),Ce(``),E(`visible`),Te(r.map(e=>e.id)),De(null),ke(null),Ae(!1),ve(!0)}'
r_qe = 'qe=()=>{ye(null),xe(``),Ce(``),E(`visible`),Te(r.map(e=>e.id)),De(null),ke(null),Ae(!1),ve(!0),setTimeout(()=>{let el=document.getElementById("sami_dmc_input");if(el)el.value=""},40)}'
assert t_qe in content, "t_qe not found"
content = content.replace(t_qe, r_qe)

t_ze = 'Ze=async e=>{if(e.preventDefault(),!be.trim())Ve(`يرجى إدخال اسم القناة`,!0);else try{T?(await tw(T.id,{name:be.trim(),password:Se.trim(),visibility:we,memberIds:D,imageFileOrDataUrl:Ee,removeImage:O}),Ve(`تم تحديث بيانات القناة بنجاح`)):(await ew({name:be.trim(),password:Se.trim(),visibility:we,memberIds:D,imageFileOrDataUrl:Ee}),Ve(`تم إنشاء القناة الجديدة بنجاح`)),ve(!1)}catch{Ve(`تعذر حفظ بيانات القناة`,!0)}}'
r_ze = 'Ze=async e=>{if(e.preventDefault(),!be.trim())Ve(`يرجى إدخال اسم القناة`,!0);else try{let _dVal=document.getElementById("sami_dmc_input")?.value?.trim(),_dNum=_dVal?parseInt(_dVal,10):null;if(isNaN(_dNum))_dNum=null;T?(await tw(T.id,{name:be.trim(),password:Se.trim(),visibility:we,memberIds:D,imageFileOrDataUrl:Ee,removeImage:O,displayMemberCount:_dNum}),fetch("/api/channels/"+T.id,{method:"PUT",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:be.trim(),visibility:we,memberIds:D,displayMemberCount:_dNum})}).catch(()=>{}),Ve(`تم تحديث بيانات القناة بنجاح`)):(await ew({name:be.trim(),password:Se.trim(),visibility:we,memberIds:D,imageFileOrDataUrl:Ee,displayMemberCount:_dNum}),fetch("/api/channels",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:be.trim(),visibility:we,memberIds:D,displayMemberCount:_dNum})}).catch(()=>{}),Ve(`تم إنشاء القناة الجديدة بنجاح`)),ve(!1)}catch{Ve(`تعذر حفظ بيانات القناة`,!0)}}'
assert t_ze in content, "t_ze not found"
content = content.replace(t_ze, r_ze)

# 11. Add displayMemberCount input to Channel Modal form JSX (Requirement 3, point 1, 3, 5)
t_form_input = '(0,$.jsxs)(`div`,{children:[(0,$.jsx)(`label`,{className:`block text-xs font-bold text-slate-300 mb-1`,children:`كلمة المرور الخاصة بالقناة`}),(0,$.jsx)(`input`,{type:`text`,value:Se,onChange:e=>Ce(e.target.value),placeholder:`كلمة مرور مستقلة لهذه القناة`,required:!0,className:`w-full bg-[#0b101a] border border-slate-700 rounded-xl px-3 py-2.5 text-xs text-white outline-none focus:border-amber-400`})]})'
r_form_input = t_form_input + ',(0,$.jsxs)(`div`,{children:[(0,$.jsx)(`label`,{className:`block text-xs font-bold text-amber-300 mb-1`,children:`العدد الافتراضي للأعضاء المعروض للمستخدمين (مخصص للعرض):`}),(0,$.jsx)(`input`,{id:`sami_dmc_input`,type:`number`,min:`0`,placeholder:`مثال: 2400 أو 15000 أو 1200000`,defaultValue:T?.displayMemberCount!=null?T.displayMemberCount:``,className:`w-full bg-[#0b101a] border border-amber-500/40 rounded-xl px-3 py-2.5 text-xs text-white outline-none focus:border-amber-400 font-[\'JetBrains_Mono\',monospace]`}),(0,$.jsx)(`span`,{className:`block text-[10px] text-slate-400 mt-1`,children:`رقم مخصص للعرض فقط، يدعم الأعداد الكبيرة ويتم تنسيقه تلقائياً (مثال: 2400 تظهر 2.4 ألف، 15000 تظهر 15 ألف، 1200000 تظهر 1.2 مليون).`})]})'
assert t_form_input in content, "t_form_input not found"
content = content.replace(t_form_input, r_form_input)

# 12. App update popup condition (Tw) (Requirement 4, point 3)
t_tw_fn = 'function Tw(e,t=11,n=Sw){return e?!!(e.versionCode>t||ww(e.versionName,n)):!1}'
r_tw_fn = 'function Tw(e,t=11,n=Sw){if(!e||e.isActive===false||e.isHidden===true)return!1;return!!(e.versionCode>t||ww(e.versionName,n))}'
assert t_tw_fn in content, "t_tw_fn not found"
content = content.replace(t_tw_fn, r_tw_fn)

# 13. Ew real-time updater (preserve isActive & isHidden) (Requirement 4, point 4 & 7)
t_ew_p1 = 'isMandatory:!!d.update.isMandatory,minSupportedVersionCode:d.update.minSupportedVersionCode?Number(d.update.minSupportedVersionCode):void 0,updatedAt:d.update.updatedAt?Number(d.update.updatedAt):Date.now()})'
r_ew_p1 = 'isMandatory:!!d.update.isMandatory,minSupportedVersionCode:d.update.minSupportedVersionCode?Number(d.update.minSupportedVersionCode):void 0,updatedAt:d.update.updatedAt?Number(d.update.updatedAt):Date.now(),isActive:d.update.isActive!==false&&!d.update.isHidden,isHidden:!!d.update.isHidden||d.update.isActive===false})'
assert t_ew_p1 in content, "t_ew_p1 not found"
content = content.replace(t_ew_p1, r_ew_p1)

t_ew_p2 = 'isMandatory:!!t.isMandatory,minSupportedVersionCode:t.minSupportedVersionCode?Number(t.minSupportedVersionCode):void 0,updatedAt:t.updatedAt?Number(t.updatedAt):Date.now()})'
r_ew_p2 = 'isMandatory:!!t.isMandatory,minSupportedVersionCode:t.minSupportedVersionCode?Number(t.minSupportedVersionCode):void 0,updatedAt:t.updatedAt?Number(t.updatedAt):Date.now(),isActive:t.isActive!==false&&!t.isHidden,isHidden:!!t.isHidden||t.isActive===false})'
assert t_ew_p2 in content, "t_ew_p2 not found"
content = content.replace(t_ew_p2, r_ew_p2)

# 14. Owner update status card in control panel (Requirement 4, point 1)
t_up_card = '(0,$.jsxs)(`div`,{className:`bg-[#0b0f17] p-3 rounded-xl border border-slate-800 flex items-center justify-between`,children:[(0,$.jsx)(`span`,{className:`text-slate-400`,children:`الإصدار المنشور بالسحابة:`}),(0,$.jsxs)(`span`,{className:`font-black ${l&&l.versionCode>11?`text-emerald-400`:`text-slate-300`}`,children:[`v`,l?.versionName||`1.2.0`,` (`,l?.isMandatory?`إجباري ⚠️`:`اختياري ✨`,`)`]})]})'
r_up_card = '(0,$.jsxs)(`div`,{className:`bg-[#0b0f17] p-3 rounded-xl border border-slate-800 flex items-center justify-between gap-2`,children:[(0,$.jsx)(`span`,{className:`text-slate-400`,children:`الإصدار بالسحابة:`}),(0,$.jsxs)(`span`,{className:`font-black ${l&&l.versionCode>11?`text-emerald-400`:`text-slate-300`}`,children:[`v`,l?.versionName||`1.3.1`,` (`,l?.isMandatory?`إجباري ⚠️`:`اختياري ✨`,`)`]}),(0,$.jsx)(`span`,{className:`text-[11px] font-black px-2 py-0.5 rounded-lg ${l&&l.isActive!==false&&!l.isHidden?`bg-emerald-500/20 text-emerald-400 border border-emerald-500/40`:`bg-rose-500/20 text-rose-400 border border-rose-500/40`}`,children:l&&l.isActive!==false&&!l.isHidden?`🟢 معروض للجميع`:`⏸️ متوقف ومخفي`})]})'
assert t_up_card in content, "t_up_card not found"
content = content.replace(t_up_card, r_up_card)

# 15. Toggle visibility button in Owner control panel (Requirement 4, point 2, 5, 8, 10)
t_up_btn = '(0,$.jsx)(`button`,{type:`button`,onClick:async()=>{f(`1.2.0`),m(`10`),x(!1),ee(!0);try{await Dw({versionName:`1.2.0`,versionCode:10,downloadUrl:h.trim(),description:`الإصدار الأحدث متوفر الآن مع تحسينات في الأداء وتطوير الواجهة.`,isMandatory:!1}),Ve(`تم إيقاف التحديث وإعادة الحالة إلى v1.2.0`)}catch{Ve(`تعذر إيقاف التحديث`,!0)}finally{ee(!1)}},className:`flex-1 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-slate-200 font-bold text-xs border border-slate-800 transition cursor-pointer`,children:`إيقاف التحديث (إعادة لـ 1.2.0)`})'
r_up_btn = '(0,$.jsx)(`button`,{type:`button`,disabled:S,onClick:async()=>{ee(!0);try{let _isAct=!(l&&l.isActive!==false&&!l.isHidden);let tk="";try{let ss=localStorage.getItem("sami_auth_user_session");if(ss)tk=JSON.parse(ss).token||""}catch(_){}let hd={"Content-Type":"application/json"};if(tk)hd["Authorization"]="Bearer "+tk;let res=await fetch("/api/app-updates/toggle",{method:"POST",headers:hd,body:JSON.stringify({isActive:_isAct,updateId:"latest"})});let data=await res.json();if(!res.ok||!data.success)throw new Error(data.error||"فشل تحديث حالة الظهور في الخادم");try{await ov(K(Z,"app_updates","latest"),{isActive:_isAct,isHidden:!_isAct,updatedAt:Date.now()})}catch(_){}u(prev=>prev?{...prev,isActive:_isAct,isHidden:!_isAct}:null);Ve(_isAct?"تمت إعادة إظهار التحديث ومزامنته للمستخدمين بنجاح ✅":"تم إيقاف ظهور التحديث وإخفاؤه عن جميع المستخدمين بنجاح ⏸️")}catch(err){Ve(err?.message||"تعذر تغيير حالة ظهور التحديث",!0)}finally{ee(!1)}},className:`flex-1 py-2.5 rounded-xl font-black text-xs border transition cursor-pointer flex items-center justify-center gap-1.5 ${l&&l.isActive!==false&&!l.isHidden?"bg-rose-500/15 hover:bg-rose-500/25 border-rose-500/40 text-rose-300":"bg-emerald-500/20 hover:bg-emerald-500/30 border-emerald-500/40 text-emerald-300"}`,children:l&&l.isActive!==false&&!l.isHidden?"⏸️ إيقاف ظهور التحديث عن المستخدمين":"▶️ إعادة إظهار التحديث للمستخدمين"})'
assert t_up_btn in content, "t_up_btn not found"
content = content.replace(t_up_btn, r_up_btn)

with open('public/assets/index-DoqMLvwt.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: All updates successfully applied to public/assets/index-DoqMLvwt.js")
