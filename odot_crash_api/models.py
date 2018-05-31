from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class CrashHr(models.Model):
    crash_hr_no = models.IntegerField(primary_key=True)
    crash_hr_long_desc = models.TextField(blank=True, null=True)
    crash_hr_med_desc = models.TextField(blank=True, null=True)
    crash_hr_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_hr'
        in_db = 'odot_crash_data'

class CrashSvrty(models.Model):
    crash_svrty_cd = models.IntegerField(primary_key=True)
    crash_svrty_long_desc = models.TextField(blank=True, null=True)
    crash_svrty_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_svrty'
        in_db = 'odot_crash_data'


class CrashTyp(models.Model):
    crash_typ_cd = models.TextField(primary_key=True)
    crash_typ_long_desc = models.TextField(blank=True, null=True)
    crash_typ_med_desc = models.TextField(blank=True, null=True)
    crash_typ_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_typ'
        in_db = 'odot_crash_data'

class CollisTyp(models.Model):
    collis_typ_cd = models.TextField(primary_key=True)
    collis_typ_long_desc = models.TextField(blank=True, null=True)
    collis_typ_alt_long_desc = models.TextField(blank=True, null=True)
    collis_typ_med_desc = models.TextField(blank=True, null=True)
    collis_typ_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collis_typ'

class Crash(models.Model):
    crash_id = models.IntegerField(primary_key=True)
    ser_no = models.TextField(blank=True, null=True)
    crash_dt = models.TextField(blank=True, null=True)
    crash_mo_no = models.IntegerField(blank=True, null=True)
    crash_day_no = models.IntegerField(blank=True, null=True)
    crash_yr_no = models.IntegerField(blank=True, null=True)
    crash_wk_day_cd = models.IntegerField(blank=True, null=True)
    crash_hour = models.ForeignKey(
        CrashHr, on_delete=models.CASCADE, db_column="crash_hr_no", related_name="crash_hour")
    cnty_id = models.IntegerField(blank=True, null=True)
    cnty_nm = models.TextField(blank=True, null=True)
    city_sect_id = models.IntegerField(blank=True, null=True)
    city_sect_nm = models.TextField(blank=True, null=True)
    urb_area_cd = models.IntegerField(blank=True, null=True)
    urb_area_short_nm = models.TextField(blank=True, null=True)
    fc_cd = models.IntegerField(blank=True, null=True)
    fc_short_desc = models.TextField(blank=True, null=True)
    nhs_flg = models.IntegerField(blank=True, null=True)
    hwy_no = models.IntegerField(blank=True, null=True)
    hwy_sfx_no = models.NullBooleanField()
    hwy_med_nm = models.TextField(blank=True, null=True)
    rdwy_no = models.IntegerField(blank=True, null=True)
    hwy_compnt_cd = models.IntegerField(blank=True, null=True)
    hwy_compnt_short_desc = models.TextField(blank=True, null=True)
    mlge_typ_cd = models.IntegerField(blank=True, null=True)
    mlge_typ_short_desc = models.TextField(blank=True, null=True)
    rd_con_no = models.IntegerField(blank=True, null=True)
    lrs_val = models.TextField(blank=True, null=True)
    lat_deg_no = models.IntegerField(blank=True, null=True)
    lat_minute_no = models.IntegerField(blank=True, null=True)
    lat_sec_no = models.FloatField(blank=True, null=True)
    longtd_deg_no = models.IntegerField(blank=True, null=True)
    longtd_minute_no = models.IntegerField(blank=True, null=True)
    longtd_sec_no = models.FloatField(blank=True, null=True)
    lat_dd = models.FloatField(blank=True, null=True)
    longtd_dd = models.FloatField(blank=True, null=True)
    specl_jrsdct_id = models.NullBooleanField()
    specl_jrsdct_short_desc = models.NullBooleanField()
    jrsdct_grp_cd = models.NullBooleanField()
    jrsdct_grp_long_desc = models.NullBooleanField()
    agy_st_no = models.TextField(blank=True, null=True)
    st_full_nm = models.TextField(blank=True, null=True)
    recre_rd_nm = models.NullBooleanField()
    isect_agy_st_no = models.TextField(blank=True, null=True)
    isect_st_full_nm = models.TextField(blank=True, null=True)
    isect_recre_rd_nm = models.NullBooleanField()
    isect_seq_no = models.IntegerField(blank=True, null=True)
    from_isect_dstnc_qty = models.IntegerField(blank=True, null=True)
    cmpss_dir_cd = models.IntegerField(blank=True, null=True)
    mp_no = models.FloatField(blank=True, null=True)
    post_speed_lmt_val = models.IntegerField(blank=True, null=True)
    rd_char_cd = models.IntegerField(blank=True, null=True)
    rd_char_short_desc = models.TextField(blank=True, null=True)
    off_rdwy_flg = models.IntegerField(blank=True, null=True)
    isect_typ_cd = models.IntegerField(blank=True, null=True)
    isect_typ_short_desc = models.TextField(blank=True, null=True)
    isect_rel_flg = models.IntegerField(blank=True, null=True)
    rndabt_flg = models.IntegerField(blank=True, null=True)
    drvwy_rel_flg = models.IntegerField(blank=True, null=True)
    ln_qty = models.IntegerField(blank=True, null=True)
    turng_leg_qty = models.IntegerField(blank=True, null=True)
    medn_typ_cd = models.IntegerField(blank=True, null=True)
    medn_typ_short_desc = models.TextField(blank=True, null=True)
    impct_loc_cd = models.IntegerField(blank=True, null=True)
    crash_type = models.ForeignKey(
        CrashTyp, on_delete=models.CASCADE, db_column="crash_typ_cd", related_name="crash_typ")
    collision_type = models.ForeignKey(
        CollisTyp, on_delete=models.CASCADE, db_column="collis_typ_cd", related_name="collis_typ")
    crash_severity = models.ForeignKey(
        CrashSvrty, on_delete=models.CASCADE, db_column="crash_svrty_cd", related_name="crash_svrty")
    wthr_cond_cd = models.IntegerField(blank=True, null=True)
    wthr_cond_short_desc = models.TextField(blank=True, null=True)
    rd_surf_cond_cd = models.IntegerField(blank=True, null=True)
    rd_surf_short_desc = models.TextField(blank=True, null=True)
    lgt_cond_cd = models.IntegerField(blank=True, null=True)
    lgt_cond_short_desc = models.TextField(blank=True, null=True)
    traf_cntl_device_cd = models.IntegerField(blank=True, null=True)
    traf_cntl_device_short_desc = models.TextField(blank=True, null=True)
    traf_cntl_func_flg = models.IntegerField(blank=True, null=True)
    invstg_agy_cd = models.IntegerField(blank=True, null=True)
    invstg_agy_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_1_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_1_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_2_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_2_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_3_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_3_short_desc = models.TextField(blank=True, null=True)
    crash_cause_1_cd = models.IntegerField(blank=True, null=True)
    crash_cause_1_short_desc = models.TextField(blank=True, null=True)
    crash_cause_2_cd = models.IntegerField(blank=True, null=True)
    crash_cause_2_short_desc = models.TextField(blank=True, null=True)
    crash_cause_3_cd = models.IntegerField(blank=True, null=True)
    crash_cause_3_short_desc = models.TextField(blank=True, null=True)
    schl_zone_ind = models.IntegerField(blank=True, null=True)
    wrk_zone_ind = models.IntegerField(blank=True, null=True)
    alchl_invlv_flg = models.IntegerField(blank=True, null=True)
    drug_invlv_flg = models.IntegerField(blank=True, null=True)
    crash_speed_invlv_flg = models.IntegerField(blank=True, null=True)
    crash_hit_run_flg = models.IntegerField(blank=True, null=True)
    pop_rng_cd = models.IntegerField(blank=True, null=True)
    pop_rng_med_desc = models.TextField(blank=True, null=True)
    rd_cntl_cd = models.IntegerField(blank=True, null=True)
    rd_cntl_med_desc = models.TextField(blank=True, null=True)
    rte_typ_cd = models.TextField(blank=True, null=True)
    rte_id = models.TextField(blank=True, null=True)
    rte_nm = models.TextField(blank=True, null=True)
    reg_id = models.IntegerField(blank=True, null=True)
    dist_id = models.TextField(blank=True, null=True)
    seg_mrk_id = models.TextField(blank=True, null=True)
    seg_pt_lrs_meas = models.FloatField(blank=True, null=True)
    unloct_flg = models.IntegerField(blank=True, null=True)
    crash_last_ud_dt = models.TextField(blank=True, null=True)
    tot_vhcl_cnt = models.IntegerField(blank=True, null=True)
    tot_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_b_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_c_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_uninjd_age00_04_cnt = models.IntegerField(blank=True, null=True)
    tot_uninjd_per_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_occup_cnt = models.IntegerField(blank=True, null=True)
    tot_per_invlv_cnt = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_used_qty = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_unused_qty = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_use_unknown_qty = models.IntegerField(blank=True, null=True)
    tot_psngr_vhcl_occ_unrestrnd_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_unhelmtd_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_alchl_impaired_drvr_inv_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_drvr_age_01_20_cnt = models.IntegerField(blank=True, null=True)
    lane_rdwy_dprt_crash_flg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash'
        in_db = 'odot_crash_data'

class Participant(models.Model):
    crash_info = models.ForeignKey(
        Crash, on_delete=models.CASCADE, db_column="crash_id", related_name="crash")
    vhcl_id = models.IntegerField(blank=True, null=True)
    partic_id = models.IntegerField(primary_key=True)
    partic_dsply_seq_no = models.IntegerField(blank=True, null=True)
    vhcl_coded_seq_no = models.IntegerField(blank=True, null=True)
    partic_vhcl_seq_no = models.IntegerField(blank=True, null=True)
    partic_typ_cd = models.IntegerField(blank=True, null=True)
    partic_typ_short_desc = models.TextField(blank=True, null=True)
    partic_hit_run_flg = models.IntegerField(blank=True, null=True)
    pub_empl_flg = models.IntegerField(blank=True, null=True)
    sex_cd = models.IntegerField(blank=True, null=True)
    age_val = models.IntegerField(blank=True, null=True)
    drvr_lic_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_lic_stat_short_desc = models.TextField(blank=True, null=True)
    drvr_res_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_res_short_desc = models.TextField(blank=True, null=True)
    inj_svrty_cd = models.IntegerField(blank=True, null=True)
    inj_svrty_short_desc = models.TextField(blank=True, null=True)
    sfty_equip_use_cd = models.IntegerField(blank=True, null=True)
    sfty_equip_use_short_desc = models.TextField(blank=True, null=True)
    airbag_deploy_ind = models.IntegerField(blank=True, null=True)
    mvmnt_cd = models.IntegerField(blank=True, null=True)
    mvmnt_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_from_cd = models.IntegerField(blank=True, null=True)
    partic_cmpss_dir_from_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_to_cd = models.IntegerField(blank=True, null=True)
    partic_cmpss_dir_to_short_desc = models.TextField(blank=True, null=True)
    non_motrst_loc_cd = models.IntegerField(blank=True, null=True)
    non_motrst_loc_short_desc = models.TextField(blank=True, null=True)
    actn_cd = models.IntegerField(blank=True, null=True)
    actn_short_desc = models.TextField(blank=True, null=True)
    partic_err_1_cd = models.IntegerField(blank=True, null=True)
    partic_err_1_short_desc = models.TextField(blank=True, null=True)
    partic_err_2_cd = models.IntegerField(blank=True, null=True)
    partic_err_2_short_desc = models.TextField(blank=True, null=True)
    partic_err_3_cd = models.IntegerField(blank=True, null=True)
    partic_err_3_short_desc = models.TextField(blank=True, null=True)
    partic_cause_1_cd = models.IntegerField(blank=True, null=True)
    partic_cause_1_short_desc = models.TextField(blank=True, null=True)
    partic_cause_2_cd = models.IntegerField(blank=True, null=True)
    partic_cause_2_short_desc = models.TextField(blank=True, null=True)
    partic_cause_3_cd = models.IntegerField(blank=True, null=True)
    partic_cause_3_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_1_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_1_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_2_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_2_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_3_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_3_short_desc = models.NullBooleanField()
    bac_val = models.IntegerField(blank=True, null=True)
    alchl_use_rpt_ind = models.IntegerField(blank=True, null=True)
    drug_use_rpt_ind = models.IntegerField(blank=True, null=True)
    strikg_partic_flg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partic'
        in_db = 'odot_crash_data'


class Vehicle(models.Model):
    crash_info = models.ForeignKey(
        Crash, on_delete=models.CASCADE, db_column="crash_id", related_name="crash_id_no")
    vhcl_id = models.IntegerField(primary_key=True)
    vhcl_coded_seq_no = models.IntegerField(blank=True, null=True)
    vhcl_ownshp_cd = models.IntegerField(blank=True, null=True)
    vhcl_ownshp_short_desc = models.TextField(blank=True, null=True)
    vhcl_use_cd = models.IntegerField(blank=True, null=True)
    vhcl_use_short_desc = models.TextField(blank=True, null=True)
    vhcl_typ_cd = models.IntegerField(blank=True, null=True)
    vhcl_typ_short_desc = models.TextField(blank=True, null=True)
    emrgcy_vhcl_use_flg = models.IntegerField(blank=True, null=True)
    trlr_qty = models.IntegerField(blank=True, null=True)
    mvmnt_cd = models.IntegerField(blank=True, null=True)
    mvmnt_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_from_cd = models.IntegerField(blank=True, null=True)
    vhcl_cmpss_dir_from_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_to_cd = models.IntegerField(blank=True, null=True)
    vhcl_cmpss_dir_to_short_desc = models.TextField(blank=True, null=True)
    actn_cd = models.IntegerField(blank=True, null=True)
    actn_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_1_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_1_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_2_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_2_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_3_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_3_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_1_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_1_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_2_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_2_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_3_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_3_short_desc = models.TextField(blank=True, null=True)
    vhcl_speed_flg = models.IntegerField(blank=True, null=True)
    vhcl_hit_run_flg = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_used_qty = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_unused_qty = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_use_unknwn_qty = models.IntegerField(blank=True, null=True)
    vhcl_occup_cnt = models.IntegerField(blank=True, null=True)
    strikg_vhcl_flg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhcl'
        in_db = 'odot_crash_data'
