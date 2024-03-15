class matematica:
    
    def somar (v1, v2):
        return v1 + v2
    
pytest.main(["-v", "--tb=line", "-rN", __file__])