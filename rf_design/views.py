from pathlib import Path
from django.shortcuts import render
import passive_auto_design.components.coupler as cpl
import passive_auto_design.substrate as sub

modul_dir = Path(__file__).resolve(strict=True).parents[1]

def index(request):
    return render(request, 'rf/index.html')

def coupler_sizing(request):
    context = {}
    try:
        z_c = request.POST.get('z_c', 50)
        context.update({'z_c': z_c})
        k = request.POST.get('k', 0.9)
        context.update({'k': k})
        freq = request.POST.get('frequence', 10)
        context.update({'freq': freq})
        
        BEOL = sub.Substrate(modul_dir / 'tech.yml')
        CPL = cpl.Coupler(BEOL)
        CPL.z_c = float(z_c)
        CPL.f_c = float(freq)*1e9
        CPL.design(0)
        CPL.transfo.set_primary(CPL.transfo.prim)
        result = {'lp': round(CPL.transfo.model["lp"]*1e9, 3),
                  'rp': round(CPL.transfo.model["rp"], 3),
                  'cg': round(CPL.transfo.model["cg"]*1e15, 3),
                  'cm': round(CPL.transfo.model["cm"]*1e15, 3),
            }
        context.update({'result': result})
    except Exception as e:
        context.update({'result': repr(e)})
    return render(request, 'rf/model_extraction.html')

def model_ext(request):
    return render(request, 'rf/coupler_sizing.html')
