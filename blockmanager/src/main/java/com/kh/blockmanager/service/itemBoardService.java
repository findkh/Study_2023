package com.kh.blockmanager.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.kh.blockmanager.mapper.itemBoardMapper;

@Service
public class itemBoardService {
	
	@Autowired
	private itemBoardMapper mapper;
	
	public List<Map<String,Object>> getItemList() {
		return mapper.getItemList();
	}

}
