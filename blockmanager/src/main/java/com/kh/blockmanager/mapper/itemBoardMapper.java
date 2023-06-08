package com.kh.blockmanager.mapper;

import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

@Repository
public interface itemBoardMapper {
	List<Map<String,Object>> getItemList();
}
