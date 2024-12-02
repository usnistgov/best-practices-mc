#for fig in ['detailed_balance2', 'lhs_nvt', 'npt', 'muvt', 'energybias2', 'avb', 'avb2', 'avb4', 'dccb_draw', 'cluster2']:
#for fig in 'detailed_balance2' 'lhs_nvt' 'npt' 'muvt2' 'muvt_target' 'energybias2' 'avb' 'avb2' 'avb4' 'dccb_draw' 'cluster2' 'cavity'; do
for fig in `ls *py`; do
  echo $fig
  python $fig
done
